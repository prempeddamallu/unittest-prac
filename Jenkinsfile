pipeline{
    agent any
    environment{
        IMAGE_NAME = 'unit-test-prac'
        IMAGE_TAG = '1.0'
        CONTAINER_NAME = 'unit-container'
    }
    stages{
        stage("Checkout Code"){
            steps{
                script{
                    checkout scm
                }
            }
        }
        stage("Build Image"){
            steps{
                script{
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }
        stage("Run Cotainer"){
            steps{
                script{
                    sh "docker run --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }

    post{
        always{
            sh "docker rm ${CONTAINER_NAME} || true"
            sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
        success{
            echo "Build and tests were successful"
        }
        failure{
            echo "Build and tests were failed"
        }
    }
}