// deploy_mcp -- deploys the prog-validate MCP service to eliozo.dudajevagatve.lv
//
// Why this is a pipeline of its own (and not just a stage of deploy_eliozo):
//
//   * The MCP service is a SEPARATE PROCESS from the Flask app -- its own
//     systemd unit (prog-validate, uvicorn/ASGI on 127.0.0.1:8001), reverse
//     proxied by Nginx at /mcp. Restarting it does not touch Gunicorn and vice
//     versa, so MCP-only changes (new tool, edited data/ file) should not
//     require a full web-app deploy + Gunicorn restart.
//   * MCP data changes are frequent and cheap: the index rebuild takes <1 s.
//
// But the two are NOT fully independent, because the MCP code lives INSIDE
// eliozoapp/ and the two share one git repo, one deployment tree and one
// virtualenv. deploy_eliozo rsyncs all of eliozoapp/ with --delete, so it
// necessarily overwrites mcp/ too. That is why deploy_eliozo has a DEPLOY_MCP
// parameter that calls the same root helper this pipeline calls -- otherwise a
// web deploy would leave the MCP service running stale code with a deleted
// index.
//
// Rule of thumb:
//   changed only mcp/**            -> run deploy_mcp
//   changed the Flask app (or both) -> run deploy_eliozo with DEPLOY_MCP=true
//
// Server prerequisite (one time):
//   sudo bash /home/kalvis/workspace/eliozo-setup/scripts/setup-mcp-jenkins-deploy.sh
// which installs /usr/local/bin/deploy-mcp and the jenkins sudoers grant.

pipeline {
    agent any

    environment {
        MCP_HELPER = '/usr/local/bin/deploy-mcp'
        PUBLIC_URL = 'https://eliozo.dudajevagatve.lv/mcp'
    }

    parameters {
        choice(
            name: 'BRANCH_OR_TAG',
            choices: [
                '*/main',
                'refs/tags/eliozo-1.0'
            ],
            description: 'Revision of eliozo/qualification-project to deploy'
        )
        booleanParam(
            name: 'RUN_PREFLIGHT',
            defaultValue: true,
            description: 'Build the index (and run the acceptance tests) in the ' +
                         'Jenkins workspace before touching production. Catches a ' +
                         'broken data/ file here instead of failing the service start.'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                cleanWs()
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.BRANCH_OR_TAG]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/eliozo/qualification-project.git'
                    ]]
                ])
            }
        }

        // Fail here rather than on the server. build_index.py is also the
        // consistency check: it errors out if a curriculum cites a standard code
        // that does not exist. Since the systemd unit reruns it as ExecStartPre,
        // a bad data/ file would otherwise take the live service DOWN.
        stage('Pre-flight (index + tests)') {
            when { expression { params.RUN_PREFLIGHT } }
            steps {
                sh '''
                set -eu
                cd eliozoapp/mcp/prog-validate

                PY="${ELIOZO_PYTHON_ENV:-python3}"
                echo "Pre-flight interpreter: ${PY}"

                # build_index.py needs only stdlib + PyYAML.
                "${PY}" build_index.py --out "${WORKSPACE}/.preflight-index"

                # Acceptance tests are optional here: they need the `mcp` package,
                # which the Jenkins interpreter may not have. Never block a deploy
                # on a missing test dependency -- say so instead.
                if "${PY}" -c "import mcp, pytest" 2>/dev/null; then
                    "${PY}" -m pytest tests/ -q
                else
                    echo "NOTE: 'mcp'/'pytest' not available to ${PY} -- skipping tests/."
                    echo "      The index build above still ran and passed."
                fi
                '''
            }
        }

        stage('Deploy MCP') {
            steps {
                // The helper runs as root and does: rsync (keeping the generated
                // index/), chown to eliozo:www-data, pip install the MCP
                // requirements into the shared venv, restart prog-validate (whose
                // ExecStartPre rebuilds the index), then smoke-test.
                sh """
                sudo -n '${env.MCP_HELPER}' '${env.WORKSPACE}/eliozoapp/mcp'
                """
            }
        }

        // Deliberately a Groovy ''' block with no ${} interpolation and no
        // backslash line-continuations: PUBLIC_URL comes from environment{} as a
        // real shell variable, and Groovy would otherwise consume the escapes
        // before the shell sees them.
        stage('Verify public endpoint') {
            steps {
                sh '''
                set -eu
                ACCEPT='Accept: application/json, text/event-stream'
                CT='Content-Type: application/json'
                INIT='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"jenkins","version":"1"}}}'

                SID=$(curl -sS -D - -o /dev/null -X POST "${PUBLIC_URL}" -H "${CT}" -H "${ACCEPT}" -d "${INIT}" | grep -i "^mcp-session-id" | tr -d '\\r' | awk '{print $2}')

                if [ -z "${SID}" ]; then
                    echo "ERROR: no mcp-session-id from ${PUBLIC_URL} -- handshake failed." >&2
                    echo "       A 421 here means the Host is not in the MCP SDK DNS-rebinding" >&2
                    echo "       allow-list (see PROG_VALIDATE_ALLOWED_HOSTS)." >&2
                    exit 1
                fi

                curl -sS -o /dev/null -X POST "${PUBLIC_URL}" -H "${CT}" -H "${ACCEPT}" -H "mcp-session-id: ${SID}" -d '{"jsonrpc":"2.0","method":"notifications/initialized"}'

                TOOLS=$(curl -sS -X POST "${PUBLIC_URL}" -H "${CT}" -H "${ACCEPT}" -H "mcp-session-id: ${SID}" -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}')
                echo "${TOOLS}"

                for t in list_programs list_temati get_sr_matrix; do
                    if ! echo "${TOOLS}" | grep -q "\\"${t}\\""; then
                        echo "ERROR: tool ${t} missing from tools/list" >&2
                        exit 1
                    fi
                done
                echo "OK: all three tools are published at ${PUBLIC_URL}"
                '''
            }
        }
    }

    post {
        failure {
            // `systemctl status` needs no privileges; journalctl for this unit
            // does, so point at it rather than trying to run it here.
            sh 'systemctl status prog-validate --no-pager || true'
            echo 'For unit logs run on the server: sudo journalctl -u prog-validate -n 100'
        }
    }
}
