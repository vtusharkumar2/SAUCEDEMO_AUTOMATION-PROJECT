pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --disable-warnings --maxfail=1'
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