pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vtusharkumar2/SAUCEDEMO_AUTOMATION-PROJECT'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --html=report.html --self-contained-html'
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: '.', 
                    reportFiles: 'report.html', 
                    reportName: 'Test Report'
                ])
            }
        }
    }
}