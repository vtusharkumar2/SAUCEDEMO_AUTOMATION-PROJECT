pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --disable-warnings --maxfail=1'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up...'
        }
        success {
            echo '✅ All tests passed successfully!'
        }
        failure {
            echo '❌ Build failed! Check test results.'
        }
    }
}