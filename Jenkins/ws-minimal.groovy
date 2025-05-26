pipeline {
    agent any
    
    environment {
        CONFIG_DIR = '/var/lib/jenkins/hidden_files'
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
                    
                    sh """
                    rm -fr staging
                    mkdir staging
                    """ 
                    writeFile(file: "staging/query.txt", text: params.USER_QUERY, encoding: "UTF-8")
                    sh """
                    cd staging
                    export PYTHONPATH=".."
                    cp ${CONFIG_DIR}/.env .
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py create-task --query query.txt --reference task.json   
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py get-classifiers --reference task.json
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py get-problems --worksheet worksheet.json  --reference task.json
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py convert-worksheet worksheet.json worksheet.rst --reference task.json            
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py convert-worksheet worksheet.rst worksheet.docx --reference task.json
                    cd ..
                    """
                    if (!fileExists("staging/worksheet.docx")) {
                        error("Worksheet staging/worksheet.docx not created")
                    }
                    echo("End: Creating a worksheet")
                }
            }
        }
    }


    post {
        always {
            script {
                echo("Start: Publish artifacts")
                files = ["staging/task.json", "staging/worksheet.json", "staging/worksheet.docx"]

                for (file in files) {
                    if (fileExists(file)) {
                        archiveArtifacts(artifacts: file, allowEmptyArchive: false)
                    } 
                    else {
                        echo("File ${file} not found and not published.")
                    }
                }
                echo("End: Publish artifacts")
            }
        }

        success {
            script {
                echo("Success: Pipeline succeeded; staging/worksheet.docx uploaded.")
            }
        }

        failure {
            script {
                echo("Failure: Pipeline failed; no worksheeet was produced.")
            }
        }
    }
}