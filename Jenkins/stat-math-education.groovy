pipeline {
    agent any
    
    environment {
        PYTHON_PATH = '/opt/myenv/bin/python'
    }
    
    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                script {
                    if (!env.PYTHON_PATH) {
                        error "Environment variable PYTHON_PATH is not set."
                    }
                    
                    echo "env.NODE_NAME=${env.NODE_NAME}"
                    
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/master"]],
                        userRemoteConfigs: [[
                            url: 'https://github.com/kapsitis/stat-math-education.git',
                            credentialsId: 'github-pat-stat-math'
                        ]],
                        extensions: [
                            [$class: 'RelativeTargetDirectory', relativeTargetDir: 'stat-math-education']
                        ]
                    ])

                    // dir('stat-math-education') {
                    // git branch: '*/master',
                    //     url: 'https://github.com/kapsitis/stat-math-education.git',
                    //     credentialsId: 'github-pat-stat-math'
                    // }

                    echo "(1-a) End: Copy workspace for BRANCH_OR_TAG=${params.BRANCH_OR_TAG}"
                }
            }
        }

        stage('Run RScript') {
            steps {
                script {
                    echo "Start: Run RScript"
                    sh """
                    cd stat-math-education/nms-clean
                    Rscript -e 'rmarkdown::render("LV.AMO.2014-report.Rmd", output_format="pdf_document")'
                    cp LV.AMO.2014-report.pdf /var/www/html/static/eliozo/reports
                    """
                }
            }
        }
    }
}