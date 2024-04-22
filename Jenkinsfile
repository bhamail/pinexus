pipeline {
  agent { label 'pi3' }
  tools {
    maven 'Maven-3.9.6'
  }
  triggers {
    snapshotDependencies()
    pollSCM('H/55 * * * *')
  }
  stages {
    stage('Build') {
      steps {
        // Run the maven build
        sh "mvn clean package site --show-version --batch-mode"
      }
    }
    stage('Results') {
      steps {
        //junit '**/target/surefire-reports/TEST-*.xml'
        //archive 'target/*.jar'
        publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'target/site', reportFiles: 'index.html', reportName: 'Maven Site', reportTitles: ''])      }
    }
    stage ('success'){
      steps {
        script {
          currentBuild.result = 'SUCCESS'
        }
      }
    }
  }

  post {
    failure {
      script {
        currentBuild.result = 'FAILURE'
      }
    }
    always {
      mail to: 'cibuildfarm@gmail.com',
          subject: "Pipeline: ${currentBuild.fullDisplayName} - ${currentBuild.result}",
          body: "Build Result: ${currentBuild.result} - see: ${env.BUILD_URL}"
//      script {
//        emailext(body: '${DEFAULT_CONTENT}',
//            recipientProviders: [[$class: 'CulpritsRecipientProvider']],
//            subject: '${DEFAULT_SUBJECT}')
//      }
    }
  }
}
