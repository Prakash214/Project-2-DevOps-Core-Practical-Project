pipeline {
    agent any 
    stages {

        stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('dockeruser')
                DOCKER_PWORD = credentials('dockerpass')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }

        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        

         
}

}