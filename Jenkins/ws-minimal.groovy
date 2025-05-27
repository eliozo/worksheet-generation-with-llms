pipeline {
    agent any
    
    environment {
        CONFIG_DIR = '/var/lib/jenkins/hidden_files'
    }
   
    parameters {
        text(
            name: 'USER_QUERY',
            defaultValue: 'Sagatavo darba lapu 8.–9. klases skolēniem par invariantu metodi, izmantojot stāsta elementus no Vinnija Pūka pasaules. Darba lapā jābūt 1 iesildīšanās uzdevumam (ģenerē LLM), 5 galvenajiem uzdevumiem (1 no LLM, pārējie 4 adaptēti no Jena Fuseki), kā arī īsam skaidrojumam par invariantiem un piemēram. Uzdevumi jāizvieto tā, lai darba lapa nepārsniegtu 2 A4 lapas. Beigās – skolēnu ieteikumi (1–2 uzdevumu atrisināšanas padomi). Iekļauj, piemēram, kā Vinnijs Pūks mēģina sadalīt medu draugiem, bet lietas mainās pēc noteikta likuma.',
            description: 'Strukturēts vaicājums: Par ko, kam un kā veidojama darba lapa.'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                //cleanWs()
                deleteDir()
                sh "echo WORKING DIR"
                sh "pwd"
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
                            url: 'https://github.com/eliozo/worksheet-generation-with-llms.git'
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
                    cp ${CONFIG_DIR}/.env ../scripts
                    cp ../scripts/templates/regular.rst.jinja regular.rst.jinja
                    echo "CREATE-TASK KOMANDA, KURA IZVEIDO TASK.JSON, PIEVIENO DARBA LAPAI VIRSRAKSTU, KLASI U.T.T NO LIETOTĀJA VAICĀJUMA"
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py create-task --query query.txt --reference task.json
                    echo "GET-CLASSIFIERS KOMANDA, KURA PAPILDINA TASK.JSON AR TĒMU KLASIFIKATORIEM"   
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py get-classifiers --reference task.json
                    echo "GET-PROBLEMS KOMANDA, KURA IEGŪST DATUS NO SPARQL"
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py get-problems --worksheet worksheet.json  --reference task.json
                    echo "CONVERT-WORKSHEET KOMANDA, KURA PĀRVEIDO DARBA LAPU NO JSON UZ RST"
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py convert-worksheet worksheet.json worksheet.rst --template regular.rst.jinja  
                    echo "CONVERT-WORKSHEET KOMANDA, KURA PĀRVEIDO DARBA LAPU NO RST UZ DOCX"
                    ${env.PYTHON_PATH} ../scripts/eliozo_client.py convert-worksheet worksheet.rst worksheet.docx
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
                def files = ["staging/task.json", "staging/worksheet.json", "staging/worksheet1.json", "staging/worksheet.docx", "staging/regular.rst.jinja"]
                for (file in files) {
                    if (fileExists(file)) {
                        archiveArtifacts(artifacts: file, allowEmptyArchive: false)
                    } 
                    else {
                        echo("File ${file} not found and not published.")
                    }
                }
                if (fileExists("staging/worksheet.rst")) {
                    sh "cp staging/worksheet.rst staging/worksheet.rst.txt"
                    archiveArtifacts(artifacts: "staging/worksheet.rst.txt", allowEmptyArchive: false)
                } 
                else {
                    echo("File ${file} not found and not published.")
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