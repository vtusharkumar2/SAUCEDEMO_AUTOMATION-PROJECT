pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vtusharkumar2/SAUCEDEMO_AUTOMATION-PROJECT.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                // Skipping pip upgrade to avoid Windows file-locking issues
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
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