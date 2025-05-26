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
                    echo "HELLO"
                }
            }
        }
    }
}