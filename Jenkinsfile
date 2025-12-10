pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                // Checkout from your GitHub repo
                git branch: 'main', url: 'https://github.com/rohithnune13/cad_currency_cal.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Create virtual environment
                bat 'C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m venv venv'
                // Upgrade pip
                bat 'venv\\Scripts\\activate && python -m pip install --upgrade pip'
                // Install dependencies including pytest-html
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && pip install pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest with HTML report
                bat 'venv\\Scripts\\activate && pytest --html=report.html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
