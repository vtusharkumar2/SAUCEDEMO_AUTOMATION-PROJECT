pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=reports/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            // ✅ Archive HTML report
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true

            // ✅ Archive screenshots from failures
            archiveArtifacts artifacts: 'screenshots/*.png', fingerprint: true
        }
    }
}