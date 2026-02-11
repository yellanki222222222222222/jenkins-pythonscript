pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\yella\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }

        stage('Run Python') {
            steps {
                bat '"C:\\Users\\yella\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }

    }
}
