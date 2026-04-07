pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root'
        }
    }

    stages {

        stage('Print Student Info') {
            steps {
                sh '''
                echo "======================================"
                echo "Name: GOLLA NIKHIL"
                echo "Roll No: 2022BCS0077"
                echo "======================================"
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Training Script') {
            steps {
                sh '''
                . venv/bin/activate
                python train.py
                '''
            }
        }

        stage('Print Completion Message') {
            steps {
                sh '''
                echo "======================================"
                echo "Model training completed successfully!"
                echo "======================================"
                '''
            }
        }
    }
}
