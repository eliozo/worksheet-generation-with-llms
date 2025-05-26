pipeline {
    agent any
    
    environment {
        NEXUS_REPO = 'https://wc-nexus.riga.whitecryption.com/repository/contest-research'
    }
   
    parameters {
        choice(
            name: 'BRANCH_OR_TAG', 
            choices: ['aaa', 'bbb', 'ccc'], 
            description: 'Branch or tag of ContestKA repository to use in the backend'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                script {
                    echo "HELLO"
                }
            }
        }
    }
}