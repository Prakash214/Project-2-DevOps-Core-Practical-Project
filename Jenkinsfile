pipeline {
    agent any
    stages {
        stage('Run-tests') {
            steps {
                sh 'bash test.sh'
            }
        }
        stage('Build and Push'){
            environment {
                DOCKER_CREDS = credentials('dockerlogin')
            }
            steps {
                sh "sudo docker-compose build "
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "sudo docker-compose push"
                sh "sudo docker-compose up -d"
            }
        }

    }
}
