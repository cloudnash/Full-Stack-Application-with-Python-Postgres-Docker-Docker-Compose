pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/cloudnash/fullstack-devops-app.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 15'
                sh 'curl -f http://localhost:8000/docs || exit 1'
            }
        }
    }

    post {
        always {
            sh 'docker ps -a'
        }
        failure {
            echo "❌ Build failed!"
        }
        success {
            echo "✅ Application deployed successfully!"
        }
    }
}
