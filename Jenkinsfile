pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'flask-app', description: 'Docker image name')
        string(name: 'REGISTRY_URL', defaultValue: '', description: 'Optional registry URL, for example docker.io/your-user or aws-account.dkr.ecr.region.amazonaws.com')
        booleanParam(name: 'PUSH_IMAGE', defaultValue: false, description: 'Push the image to the registry')
        string(name: 'DOCKER_CREDENTIALS_ID', defaultValue: 'docker-registry', description: 'Jenkins Docker registry credentials ID')
    }

    environment {
        PYTHON_VERSION = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Python') {
            steps {
                sh '''
                    set -e
                    ${PYTHON_VERSION} --version
                    ${PYTHON_VERSION} -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def commitTag = env.GIT_COMMIT ? env.GIT_COMMIT.take(7) : 'latest'
                    env.BUILD_TAG_DOCKER = commitTag
                    def imageName = params.IMAGE_NAME

                    if (params.REGISTRY_URL?.trim()) {
                        env.DOCKER_IMAGE = "${params.REGISTRY_URL.trim().replaceAll('/+$', '')}/${imageName}:${commitTag}"
                        env.DOCKER_IMAGE_LATEST = "${params.REGISTRY_URL.trim().replaceAll('/+$', '')}/${imageName}:latest"
                    } else {
                        env.DOCKER_IMAGE = "${imageName}:${commitTag}"
                        env.DOCKER_IMAGE_LATEST = "${imageName}:latest"
                    }

                    sh '''
                        set -e
                        docker build --pull -t "${DOCKER_IMAGE}" -t "${DOCKER_IMAGE_LATEST}" .
                        docker image inspect "${DOCKER_IMAGE}" >/dev/null
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            when {
                expression { return params.PUSH_IMAGE && params.REGISTRY_URL?.trim() }
            }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: params.DOCKER_CREDENTIALS_ID,
                    usernameVariable: 'REGISTRY_USERNAME',
                    passwordVariable: 'REGISTRY_PASSWORD'
                )]) {
                    sh '''
                        set -e
                        echo "$REGISTRY_PASSWORD" | docker login "${REGISTRY_URL}" -u "$REGISTRY_USERNAME" --password-stdin
                        docker push "${DOCKER_IMAGE}"
                        docker push "${DOCKER_IMAGE_LATEST}"
                        docker logout "${REGISTRY_URL}" || true
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'rm -rf .venv' || true
        }
        success {
            echo 'Flask tests passed and Docker image build completed.'
        }
        failure {
            echo 'The pipeline failed. Review the stage logs above.'
        }
    }
}
