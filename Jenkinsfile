pipeline {
  agent any
  stages {
    stage('Checkout main branch') {
      steps {
        git(url: 'https://github.com/dhruv-pydev/expense-manager', branch: 'main')
      }
    }

    stage('List project files') {
      parallel {
        stage('List project files') {
          steps {
            sh 'ls -la'
          }
        }

        stage('List project dependencies') {
          steps {
            sh 'pip list'
          }
        }

      }
    }

  }
}