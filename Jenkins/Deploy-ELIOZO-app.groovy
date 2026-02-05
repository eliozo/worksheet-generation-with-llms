pipeline {
    agent any
    
    environment {
        CONFIG_DIR = '/var/lib/jenkins/hidden_files'
    }
   
    parameters {
        choice (
            name: 'BRANCH_OR_TAG',
            choices: [
                'refs/tags/eliozo-1.0',
                '*/main'
            ]
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


        stage ('Deploy') {
            steps {
                script {
                    writeFile file: 'eliozoapp/eliozo.env', text: """\
                        GOOGLE_CLIENT_ID=${env.GOOGLE_CLIENT_ID}
                        GOOGLE_CLIENT_SECRET=${env.GOOGLE_CLIENT_SECRET}
                        WEAVIATE_API_KEY=${env.WEAVIATE_API_KEY}
                        WEAVIATE_URL=${WEAVIATE_URL}
                        OPENAI_API_KEY=${OPENAI_API_KEY}
                        """.stripIndent()
                    sh """
                    cp eliozoapp/config-remote.py eliozoapp/config.py
                    sudo -n /usr/local/bin/deploy-eliozo '${env.WORKSPACE}/eliozoapp'
                    sudo -n systemctl restart eliozo
                    sudo -n systemctl reload nginx
                    """
                }
            }
        }
    }
}