// deploy_eliozo -- deploys the Eliozo Flask web application (and, by default,
// the prog-validate MCP service that ships inside the same eliozoapp/ tree).
//
// Two services live in this deployment tree and share one git repo, one
// virtualenv and some data sources:
//
//   Nginx --/------> Gunicorn (WSGI)  Flask       unit: eliozo-gunicorn
//        \--/mcp---> uvicorn  (ASGI)  asgi:app    unit: prog-validate
//
// The 'Deploy' stage below rsyncs ALL of eliozoapp/ with --delete, which
// includes eliozoapp/mcp/. It therefore cannot leave the MCP service alone:
// without the 'Deploy MCP' stage the uvicorn process keeps serving the code it
// loaded at its last start, i.e. a web deploy silently leaves MCP stale.
//
// MCP-only changes do not need this pipeline at all -- run 'deploy_mcp'
// instead, which skips the Gunicorn restart. See deploy_mcp.groovy.

pipeline {
    agent any

    environment {
        CONFIG_DIR    = '/var/lib/jenkins/hidden_files'
        DEPLOY_TARGET = '/home/eliozo/workspace/qualification-project/eliozoapp'
        MCP_HELPER    = '/usr/local/bin/deploy-mcp'
        // Generated on the server, .gitignore'd, and therefore absent from the
        // Jenkins workspace -- must be protected from rsync --delete.
        // Leading slash anchors the pattern to the transfer root (eliozoapp/).
        MCP_INDEX_REL = '/mcp/prog-validate/index/'
    }

    parameters {
        choice (
            name: 'BRANCH_OR_TAG',
            choices: [
                'refs/tags/eliozo-1.0',
                '*/main'
            ]
        )
        booleanParam(
            name: 'DEPLOY_MCP',
            defaultValue: true,
            description: 'Also redeploy the prog-validate MCP service (install its ' +
                         'requirements, restart the uvicorn unit, rebuild the index). ' +
                         'Leave ON unless you know the MCP service is being handled ' +
                         'separately -- the rsync above overwrites mcp/ regardless, so ' +
                         'turning this OFF leaves MCP running stale code.'
        )
    }

    stages {

        stage('Hello') {
            steps {
                script {
                    echo "Hello world!"
                }
            }
        }

        stage('Checkout') {
            steps {
                cleanWs()
                script {
                    env.PYTHON_PATH = env.ELIOZO_PYTHON_ENV
                    echo("env.NODE_NAME=${env.NODE_NAME}")
                    echo("env.PYTHON_PATH=${env.PYTHON_PATH}")
                    echo("python is ${env.ELIOZO_PYTHON_ENV}")
                    if (!env.PYTHON_PATH || "${env.PYTHON_PATH}" == "null") {
                        error("Environment variable ELIOZO_PYTHON_ENV is not set.")
                    }

                    echo("Start: Copying workspace")
                    def refSpec = params.BRANCH_OR_TAG
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: refSpec]],
                        userRemoteConfigs: [[
                            url: 'https://github.com/eliozo/qualification-project.git'
                        ]]
                    ])
                    echo("End: Copying workspace")
                }
            }
        }

        // Catch a broken curriculum/standard file before it can take the MCP
        // service down: build_index.py doubles as a consistency check and the
        // prog-validate unit reruns it as ExecStartPre on every restart.
        stage('Pre-flight MCP index') {
            when { expression { params.DEPLOY_MCP } }
            steps {
                sh '''
                set -eu
                cd eliozoapp/mcp/prog-validate
                PY="${ELIOZO_PYTHON_ENV:-python3}"
                "${PY}" build_index.py --out "${WORKSPACE}/.preflight-index"
                '''
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    writeFile file: 'eliozoapp/eliozo.env', text: """\
                        GOOGLE_CLIENT_ID=${env.GOOGLE_CLIENT_ID}
                        GOOGLE_CLIENT_SECRET=${env.GOOGLE_CLIENT_SECRET}
                        OPENAI_API_KEY=${OPENAI_API_KEY}
                        PROBLEMBASE_ROOT=${PROBLEMBASE_ROOT}
                        """.stripIndent()
                    // --exclude of the MCP index: it is generated on the server and
                    //   absent here, so --delete would otherwise wipe it on every run
                    //   (an excluded path is also protected from deletion).
                    // --chown: rsync runs as root and -a would otherwise preserve the
                    //   jenkins ownership of the workspace files. The services run as
                    //   eliozo, and prog-validate's ExecStartPre must be able to WRITE
                    //   mcp/prog-validate/index/.
                    sh """
                    cp eliozoapp/config-remote.py eliozoapp/config.py
                    sudo -n rsync -av --delete \\
                        --exclude='__pycache__/' \\
                        --exclude='*.pyc' \\
                        --exclude='${env.MCP_INDEX_REL}' \\
                        --chown=eliozo:www-data \\
                        '${env.WORKSPACE}/eliozoapp/' '${env.DEPLOY_TARGET}/'
                    sudo -n systemctl restart eliozo-gunicorn
                    sudo -n systemctl reload nginx
                    """
                }
            }
        }

        // Separate unit, separate lifecycle. The helper installs the MCP
        // requirements (mcp / PyYAML / uvicorn -- NOT in eliozoapp/requirements.txt)
        // into the shared venv and restarts prog-validate, which rebuilds the index.
        // Same helper the standalone deploy_mcp pipeline uses.
        stage('Deploy MCP') {
            when { expression { params.DEPLOY_MCP } }
            steps {
                sh """
                sudo -n '${env.MCP_HELPER}' '${env.WORKSPACE}/eliozoapp/mcp'
                """
            }
        }

        // Two things to know about these blocks:
        //   * Jenkins `sh` runs /bin/sh (dash), so no `set -o pipefail`. Never
        //     pipe a `curl -f` into `head` -- the pipeline's exit status is
        //     head's, so a failed request would pass silently. Capture first,
        //     truncate after.
        //   * No backslash line-continuations inside a Groovy ''' block: Groovy
        //     consumes "\" + newline before the shell ever sees it.
        stage('Verify') {
            steps {
                sh '''
                set -eu
                echo "-- Flask health --"
                BODY=$(curl -fsS https://eliozo.dudajevagatve.lv/health)
                echo "${BODY}" | head -c 300
                echo
                '''
                script {
                    if (params.DEPLOY_MCP) {
                        sh '''
                        set -eu
                        echo "-- MCP handshake --"
                        INIT='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"jenkins","version":"1"}}}'
                        BODY=$(curl -fsS -X POST https://eliozo.dudajevagatve.lv/mcp -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -d "${INIT}")
                        echo "${BODY}" | head -c 400
                        echo
                        echo "${BODY}" | grep -q '"serverInfo"' || { echo "ERROR: no serverInfo in MCP initialize response" >&2; exit 1; }
                        '''
                    } else {
                        echo 'DEPLOY_MCP=false: the rsync above replaced mcp/ on the ' +
                             'server but prog-validate was NOT restarted. It is still ' +
                             'serving the previously loaded code. Run deploy_mcp, or ' +
                             '`sudo systemctl restart prog-validate` on the server.'
                    }
                }
            }
        }
    }
}
