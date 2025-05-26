pipeline {
    agent any
    
    environment {
        CONFIG_DIR = '/home/eliozo/workspace/hidden_files'
    }
   
    parameters {
        text(
            name: 'USER_QUERY',
            defaultValue: '',
            description: 'Strukturēts vaicājums: Par ko, kam un kā veidojama darba lapa.'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                script {
                    env.PYTHON_PATH = env.ELIOZO_PYTHON_ENV
                    if (!env.PYTHON_PATH) {
                        error("Environment variable ELIOZO_PYTHON_ENV is not set.")
                    }
                    echo("env.NODE_NAME=${env.NODE_NAME}")
                    echo("env.PYTHON_PATH=${env.PYTHON_PATH}")

                    logInfo("(1-a) Start: Copy workspace")
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/main"]],
                        userRemoteConfigs: [[
                            url: 'https://github.com/kapsitis/worksheet-generation.git'
                        ]]
                    ])
                    echo("Workspace copied")
                }
            }
        }
    

        stage('Main') {
            steps {
                script {
                    echo("HELLO Main!")
                }
            }
        }
    }
}