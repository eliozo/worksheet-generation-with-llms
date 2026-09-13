pipeline {
    agent any

    environment {
        // Served by Nginx as /static/eliozo/images/ (see eliozo-setup REQUEST006)
        IMAGES_DEST = '/var/www/html/eliozo/images'
    }

    stages {

        stage('Checkout') {
            steps {
                cleanWs()
                script {
                    env.PYTHON_PATH = env.ELIOZO_PYTHON_ENV
                    if (!env.PYTHON_PATH || "${env.PYTHON_PATH}" == "null") {
                        error("Environment variable ELIOZO_PYTHON_ENV is not set.")
                    }
                    if (!env.OXIGRAPH_DB_PATH || "${env.OXIGRAPH_DB_PATH}" == "null") {
                        error("Environment variable OXIGRAPH_DB_PATH is not set.")
                    }

                    echo("PYTHON_PATH=${env.PYTHON_PATH}")
                    echo("OXIGRAPH_DB_PATH=${env.OXIGRAPH_DB_PATH}")

                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[
                            url: 'https://github.com/eliozo/qualification-project.git'
                        ]],
                        extensions: [
                            [$class: 'RelativeTargetDirectory', relativeTargetDir: 'qualification-project']
                        ]
                    ])

                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[
                            url: 'https://github.com/eliozo/worksheet-generation-with-llms.git'
                        ]],
                        extensions: [
                            [$class: 'RelativeTargetDirectory', relativeTargetDir: 'worksheet-generation-with-llms']
                        ]
                    ])
                }
            }
        }

        stage('Generate metadata TTL files') {
            steps {
                dir("worksheet-generation-with-llms/scripts/setup") {
                    sh "${env.PYTHON_PATH} metadata_export.py"
                }
            }
        }

        // Problems come from the Git repositories listed in
        // qualification-project/eliozoapp/problem_repositories.json -- no longer
        // from the published Google Sheet. The importer fails the build if any
        // content file yields no problems, so a bad file cannot silently empty
        // an olympiad year. It also refreshes the Nginx image directory.
        stage('Import problem repositories') {
            steps {
                dir("qualification-project/eliozoapp") {
                    sh "${env.PYTHON_PATH} -m eliozo_dao.import_problems --source git --images-dir '${env.IMAGES_DEST}'"
                }
            }
        }

        stage('Drop existing Oxigraph store') {
            steps {
                sh 'rm -rf "$OXIGRAPH_DB_PATH"'
            }
        }

        stage('Load RDF into Oxigraph') {
            steps {
                dir("qualification-project/eliozoapp") {
                    sh "${env.PYTHON_PATH} -m eliozo_dao.load_rdf"
                }
            }
        }
    }
}
