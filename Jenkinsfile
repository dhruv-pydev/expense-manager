pipeline {
  agent any
  stages {
    stage('Checkout main branch') {
      steps {
        git(url: 'https://github.com/dhruv-pydev/expense-manager', branch: 'main')
      }
    }

  }
}