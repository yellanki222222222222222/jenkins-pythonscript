pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yellanki222222222222222/jenkins-pythonscript.git'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
