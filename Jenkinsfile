pipeline {
    agent any

    // 1. 参数化构建，输入分支名
    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'master', description: '请输入要构建的分支名')
    }

    environment {
        PROJECT_NAME = 'fastapi-expense-tracker'
        REPO_URL = 'https://github.com/DaDaGuang/learning.git'  // ← 修改为你的真实仓库地址
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "拉取分支: ${params.BRANCH_NAME}"
                git branch: "${params.BRANCH_NAME}", url: "${env.REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "构建 Docker 镜像: ${env.PROJECT_NAME}:${params.BRANCH_NAME}"
                sh """
                docker build -t ${env.PROJECT_NAME}:${params.BRANCH_NAME} .
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "运行 Docker 容器: ${env.PROJECT_NAME}"
                sh """
                docker stop ${env.PROJECT_NAME} || true
                docker rm ${env.PROJECT_NAME} || true
                docker run -d --name ${env.PROJECT_NAME} -p 8000:8000 ${env.PROJECT_NAME}:${params.BRANCH_NAME}
                """
            }
        }
    }

    post {
        failure {
            echo "⚠️ 构建失败，请检查日志！"
        }
        success {
            echo "✅ 构建并运行成功！访问 http://your.server.ip:8000"
        }
    }
}
