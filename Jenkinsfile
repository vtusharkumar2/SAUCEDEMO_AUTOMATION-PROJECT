pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/vtusharkumar2/SAUCEDEMO_AUTOMATION-PROJECT.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --maxfail=1 --disable-warnings --html=report.html --self-contained-html'
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML(target: [
                    reportName: 'Test Report',
                    reportDir: '.',
                    reportFiles: 'report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: true
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo '✅ Tests passed!'
        }
        failure {
            echo '❌ Tests failed!'
        }
    }
}