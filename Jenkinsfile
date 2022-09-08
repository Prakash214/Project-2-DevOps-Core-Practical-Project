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
                sh "sudo docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
                sh "/bin/bash -c 'docker rmi \$(docker images -q)'"
            }
        }

    }
}
