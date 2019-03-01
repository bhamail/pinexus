pipeline {
  agent { label 'pi3' }
  tools {
    maven 'Maven-3.6.0'
  }
  triggers {
    snapshotDependencies()
    pollSCM('H/55 * * * *')
  }
  stages {
    stage('Build') {
      // Run the maven build
      sh "mvn clean package site -Plinkcheck"
    }
    stage('Results') {
      junit '**/target/surefire-reports/TEST-*.xml'
      archive 'target/*.jar'
    }
    post {
      failure {
        script {
          currentBuild.result = 'FAILURE'
        }
      }
      success {
        script {
          currentBuild.result = 'SUCCESS'
        }
      }
      always {
        script {
          emailext(body: '${DEFAULT_CONTENT}',
              recipientProviders: [[$class: 'CulpritsRecipientProvider']],
              subject: '${DEFAULT_SUBJECT}')
        }
      }
    }
  }
}
