pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/TarasNon/wog.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t tardocker/wog_play .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run --name score -d -p 8777:5000 tardocker/wog_play'
            }
        }
        stage('Test'){
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pip3 install webdriver-manager'
                sh 'python3 tests/e2e.py'
     
            }
        }
        stage('Docker stop') {
            steps {
                sh 'docker stop score'
            }
        }
        
        stage("docker login") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_taras', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    } 
                }
            }
        
        stage('Push in GitHub'){
            steps {
                
                sh 'docker push tardocker/wog_play'
                sh 'docker start score'
            }
        }
    }
}
