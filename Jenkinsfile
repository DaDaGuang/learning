pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', defaultValue: 'master', description: '要构建的 Git 分支')
    }

    environment {
        IMAGE_NAME = "fastapi-expense-tracker:${params.BRANCH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "拉取分支: ${params.BRANCH}"
                git branch: "${params.BRANCH}",
                    credentialsId: '0db711c0-1648-44bd-a3c1-3d49a6a286de',
                    url: 'git@github.com:DaDaGuang/learning.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "构建 Docker 镜像: ${IMAGE_NAME}"
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "启动容器: ${IMAGE_NAME}"
                sh """
                    docker stop expense_app || true
                    docker rm expense_app || true
                    docker run -d --name expense_app -p 8000:8000 ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        failure {
            echo "⚠️ 构建失败，请检查日志！"
        }
        success {
            echo "✅ 构建成功，容器已启动！"
        }
    }
}