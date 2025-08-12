pipeline {
    agent any

    stages {
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
        stage('Archive Reports & Screenshots') {
            steps {
                archiveArtifacts artifacts: 'report.html'
                archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
            }
        }
    }
}