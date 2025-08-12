pipeline {
  agent any
  environment {
    VENV = "${WORKSPACE}\\venv"
    REPORT_DIR = "${WORKSPACE}\\reports"
  }
  stages {
    stage('Prepare workspace & kill old drivers') {
      steps {
        // ensure no stuck chromedriver processes
        bat 'tasklist | findstr /I chromedriver.exe && taskkill /F /IM chromedriver.exe || echo "no chromedriver"'
        // ensure fresh workspace pieces
        bat 'if exist venv rmdir /S /Q venv'
        bat 'if exist reports rmdir /S /Q reports'
        bat 'if exist screenshots rmdir /S /Q screenshots'
      }
    }

    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup Python & deps') {
      steps {
        bat 'python --version'
        bat 'python -m venv venv'
        // activate and install
        bat 'call venv\\Scripts\\activate && python -m pip install --upgrade pip'
        bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
        bat 'if not exist reports mkdir reports'
        bat 'if not exist screenshots mkdir screenshots'
      }
    }

    stage('Run Tests') {
      steps {
        // run tests in headless mode by default; allow failures so we can archive artifacts
        bat 'call venv\\Scripts\\activate && set HEADLESS=true && pytest -q --junitxml=%REPORT_DIR%\\junit.xml --html=%REPORT_DIR%\\report.html --self-contained-html || exit /b 0'
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/**, screenshots/**', fingerprint: true
      junit 'reports/junit.xml'
    }
  }
}