pipeline {
    agent any

    environment {
        IMAGE_NAME = 'fastapi-app'
        CONTAINER_NAME = 'fastapi-container'
        APP_PORT = '8000'
    }

    stages {
        stage('拉取代码') {
            steps {
                git 'https://github.com/DaDaGuang/learning.git'  // 改成你的真实仓库地址
            }
        }

        stage('构建 Docker 镜像') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('停止并删除旧容器') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('运行新容器') {
            steps {
                sh '''
                docker run -d --name $CONTAINER_NAME -p $APP_PORT:8000 $IMAGE_NAME
                '''
            }
        }
    }
}