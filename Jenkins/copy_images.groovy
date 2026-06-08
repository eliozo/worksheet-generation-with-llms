pipeline {
    agent any

    environment {
        IMAGES_DEST = '/var/www/html/eliozo/images'
    }

    parameters {
        string(
            name: 'MATH_BRANCH',
            defaultValue: '*/master',
            description: 'Branch of kapsitis/math repository to check out'
        )
    }

    stages {

        stage('Checkout math repository') {
            steps {
                cleanWs()
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: params.MATH_BRANCH]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/kapsitis/math.git'
                    ]],
                    extensions: [
                        [$class: 'RelativeTargetDirectory', relativeTargetDir: 'math']
                    ]
                ])
            }
        }

        stage('Copy PNG images to Nginx static directory') {
            steps {
                sh '''
                    set -eu

                    PNG_FILES=$(find math/problembase -name '*.png' | wc -l)
                    echo "Found ${PNG_FILES} PNG files under math/problembase"

                    if [ "${PNG_FILES}" -gt 0 ]; then
                        find math/problembase -name '*.png' \
                            -exec cp -u --target-directory="${IMAGES_DEST}" {} +
                    fi

                    DEST_COUNT=$(find "${IMAGES_DEST}" -maxdepth 1 -name '*.png' | wc -l)
                    echo "Destination now contains ${DEST_COUNT} PNG files"
                '''
            }
        }
    }
}
