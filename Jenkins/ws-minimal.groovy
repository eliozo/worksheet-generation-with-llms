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
                    echo("Start: Creating a worksheet")
                    writeFile(file: "query.txt", text: params.USER_QUERY, encoding: "UTF-8")
                    sh """
                    cd scripts
                    export PYTHONPATH=".."
                    python eliozo_client.py create-task --query ../tests/master-demo/query-modular.txt --reference ../tests/master-demo/task-modular.json

                    # python eliozo_client.py get-classifiers --reference ../tests/master-demo/task-modular.json

                    # python eliozo_client.py get-problems --worksheet ../tests/master-demo/worksheet-modular.json  --reference ../tests/master-demo/task-modular.json

                    # python eliozo_client.py convert-worksheet ../tests/master-demo/worksheet-modular.json ../tests/master-demo/worksheet-modular.rst --reference ../tests/master-demo/task-modular.json
                    
                    # python eliozo_client.py convert-worksheet ../tests/master-demo/worksheet-modular.rst ../tests/master-demo/worksheet-modular.docx --reference ../tests/master-demo/task-modular.json
                    """
                    echo("End: Creating a worksheet")
                }
            }
        }
    }
}