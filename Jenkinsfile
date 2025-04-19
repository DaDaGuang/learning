pipeline {
    agent any

    // 1. 参数化构建，输入分支名
parameters {
    string(name: 'BRANCH', defaultValue: 'master', description: '请输入构建分支')
}

pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo "拉取分支: ${params.BRANCH}"
                git branch: "${params.BRANCH}",
                     credentialsId: 'jenkins-github-ssh',
                     url: 'git@github.com:DaDaGuang/learning.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "构建 Docker 镜像: fastapi-expense-tracker:${params.BRANCH}"
                sh "docker build -t fastapi-expense-tracker:${params.BRANCH} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "运行 Docker 容器: fastapi-expense-tracker:${params.BRANCH}"
                sh """
                    docker stop fastapi-expense-tracker || true
                    docker rm fastapi-expense-tracker || true
                    docker run -d --name fastapi-expense-tracker -p 8000:8000 fastapi-expense-tracker:${params.BRANCH}
                """
            }
        }
    }

    post {
        failure {
            echo "⚠️ 构建失败，请检查日志！"
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
