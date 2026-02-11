pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\yella\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }

        stage('Run app.py') {
            steps {
                bat '"C:\\Users\\yella\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }

        stage('Run time.py') {
            steps {
                bat '"C:\\Users\\yella\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" time.py'
            }
        } 

    }
}
