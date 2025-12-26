pipeline {
    agent any
    
    environment {
        ELIOZO_PYTHON_PATH = '/opt/myenv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                script {
                    if (!env.ELIOZO_PYTHON_ENV) {
                        error "Environment variable ELIOZO_PYTHON_ENV is not set."
                    }
                    env.PYTHON_PATH = env.ELIOZO_PYTHON_ENV
                    echo "env.NODE_NAME=${env.NODE_NAME}"
                    
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/main"]],
                        userRemoteConfigs: [[
                            url: 'https://github.com/eliozo/worksheet-generation-with-llms.git'
                        ]],
                        extensions: [
                            [$class: 'RelativeTargetDirectory', relativeTargetDir: 'worksheet-generation-with-llms']
                        ]
                    ])

                    echo "(1-a) End: Copy workspace for BRANCH_OR_TAG=${params.BRANCH_OR_TAG}"
                }
            }
        }
        
        stage('Write .env file') {
            steps {
                sh '''
                    echo "WEAVIATE_URL=$WEAVIATE_URL" > .env
                    echo "WEAVIATE_API_KEY=$WEAVIATE_API_KEY" >> .env
                    echo "OPENAI_API_KEY=$OPENAI_API_KEY" >> .env
                    echo "FUSEKI_URL=$FUSEKI_URL" >> .env
                    echo "FUSEKI_USER=$FUSEKI_USER" >> .env
                    echo "FUSEKI_PASSWORD=$FUSEKI_PASSWORD" >> .env
                    echo "DEEPSEEK_API_KEY=$DEEPSEEK_API_KEY" >> .env
                    
                '''
                sh """
                cp .env worksheet-generation-with-llms/scripts
                """
                
            }
        }

        stage('Import problems from Markdown'){
            steps {
                script {
                    echo "Izčeko math repozitoriju"
                    echo "worksheet-generation-with-llms jāizčeko"
                    sh """
                    cd worksheet-generation-with-llms/scripts/setup
                    ls -la
                    ./fuseki_setup.sh
                    ./metadata_export.sh
                    """
                    echo "Nomet esošo datubāzi"
                    echo "Apstaigā failus no math repozitorija"
                    echo "Pārveido par turtle un importē Fuseki"
                    echo "Metainformāciju eliozo metadata tabulās pārveido par RDF un arī importē"
                }
            }
        }
    }
}