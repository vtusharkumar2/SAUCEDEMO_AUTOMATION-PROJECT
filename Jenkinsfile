pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull latest code from GitHub
                git branch: 'main',
                    url: 'https://github.com/vtusharkumar2/SAUCEDEMO_AUTOMATION-PROJECT.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment in Windows
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and stop at first failure
                bat 'venv\\Scripts\\pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up...'
        }
        failure {
            echo 'Build failed! Check the test results and fix errors.'
        }
    }
}