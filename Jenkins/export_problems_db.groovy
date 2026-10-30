// export_problems_db -- dumps the problem index (PostgreSQL + pgvector tables
// problems, solution_chunks, alembic_version, embeddings included) of the
// production server and publishes it as a downloadable build artifact.
//
// Runs on the production host (Ubuntu, native PostgreSQL 16). The dump is a
// `pg_dump --format=custom` file without owners/grants, meant to initialise a
// workstation database, typically PostgreSQL in Docker on Windows 11:
//
//   python eliozo-db\scripts\pg_import_problems.py eliozo-problems-*.dump
//
// (see eliozo-setup ADMIN-GUIDE.md, "Dump / restore", and REQUEST020).
//
// Database access: OS user `jenkins` logs in as the read-only PostgreSQL role
// `jenkins` over the Unix socket by peer authentication -- no password is
// stored in Jenkins. One-time setup on the server:
//   sudo bash ~/workspace/eliozo-setup/scripts/setup-jenkins-pg-export.sh
//
// Only reads the database; safe to run at any time, also while Flask is serving.

pipeline {
    agent any

    options {
        // Each dump is ~40 MB: keep the artifacts of the last few builds only.
        buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '3'))
        disableConcurrentBuilds()
    }

    environment {
        // Read by eliozo-db/scripts/dbenv.py. There is no .env in the fresh
        // workspace, so these are the only settings. An empty DB_PASSWORD plus
        // the socket directory as DB_HOST means peer authentication.
        DB_HOST     = '/var/run/postgresql'
        DB_PORT     = '5432'
        DB_NAME     = 'eliozo'
        DB_USER     = 'jenkins'
        DB_PASSWORD = ''
    }

    stages {

        stage('Checkout') {
            steps {
                cleanWs()
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/kapsitis/eliozo-db.git'
                    ]],
                    extensions: [
                        [$class: 'RelativeTargetDirectory', relativeTargetDir: 'eliozo-db']
                    ]
                ])
            }
        }

        // Jenkins `sh` runs /bin/sh (dash): no pipefail, and no backslash
        // line-continuations inside a Groovy ''' block (Groovy eats them).
        stage('Export') {
            steps {
                sh '''
                set -eu
                rm -f eliozo-problems-*
                STAMP=$(date -u +%Y%m%d-%H%M)
                DUMP="eliozo-problems-${STAMP}.dump"
                # The export scripts use only the standard library: system python3 is enough.
                python3 eliozo-db/scripts/pg_export_problems.py --mode native -o "${DUMP}"
                echo "${DUMP}" > .dump-name
                '''
            }
        }

        // A dump that cannot be listed, or holds no problems, must not be
        // published as if it were usable.
        stage('Verify & describe') {
            steps {
                sh '''
                set -eu
                DUMP=$(cat .dump-name)
                TOC=$(pg_restore -l "${DUMP}")
                DATA=$(echo "${TOC}" | grep -c 'TABLE DATA' || true)
                [ "${DATA}" = 3 ] || { echo "ERROR: expected 3 TABLE DATA entries, found ${DATA}" >&2; exit 1; }

                Q() { psql -X -A -t -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d "${DB_NAME}" -c "$1"; }
                PROBLEMS=$(Q 'SELECT count(*) FROM problems')
                [ "${PROBLEMS}" -gt 0 ] || { echo "ERROR: the problems table is empty" >&2; exit 1; }

                sha256sum "${DUMP}" > "${DUMP}.sha256"
                {
                  echo "file:              ${DUMP}"
                  echo "sha256:            $(cut -d' ' -f1 "${DUMP}.sha256")"
                  echo "size_bytes:        $(stat -c %s "${DUMP}")"
                  echo "created_utc:       $(date -u '+%Y-%m-%d %H:%M:%S')"
                  echo "jenkins_build:     ${BUILD_TAG}"
                  echo "eliozo_db_commit:  $(git -C eliozo-db rev-parse --short HEAD)"
                  echo "server:            $(Q "SELECT split_part(version(), ' on ', 1)")"
                  echo "pg_dump:           $(pg_dump --version)"
                  echo "pgvector:          $(Q "SELECT extversion FROM pg_extension WHERE extname = 'vector'")"
                  echo "alembic_revision:  $(Q 'SELECT version_num FROM alembic_version')"
                  echo "problems:          ${PROBLEMS} ($(Q 'SELECT count(embedding) FROM problems') with embedding)"
                  echo "solution_chunks:   $(Q 'SELECT count(*) FROM solution_chunks') ($(Q 'SELECT count(embedding) FROM solution_chunks') with embedding)"
                  echo
                  echo "Restore (needs PostgreSQL 16 or newer with pgvector, e.g. Docker image pgvector/pgvector:pg16):"
                  echo "  python eliozo-db/scripts/pg_import_problems.py ${DUMP}"
                  echo "Check the download first (Windows PowerShell):"
                  echo "  Get-FileHash ${DUMP} -Algorithm SHA256"
                } > "${DUMP}.txt"
                cat "${DUMP}.txt"
                '''
            }
        }

        stage('Publish') {
            steps {
                archiveArtifacts artifacts: 'eliozo-problems-*', fingerprint: true, onlyIfSuccessful: true
            }
        }
    }
}
