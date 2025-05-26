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
                    echo("env.NODE_NAME=${env.NODE_NAME}")
                    echo("env.PYTHON_PATH=${env.PYTHON_PATH}")
                    echo("python is ${env.ELIOZO_PYTHON_ENV}")
                    if (!env.PYTHON_PATH || "${env.PYTHON_PATH}" == "null") {
                        error("Environment variable ELIOZO_PYTHON_ENV is not set.")
                    }

                    echo("Start: Copying workspace")
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/main"]],
                        userRemoteConfigs: [[
                            url: 'https://github.com/kapsitis/worksheet-generation.git'
                        ]]
                    ])
                    echo("End: Copying workspace")
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