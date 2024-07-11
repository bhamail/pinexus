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
      steps {
        // Run the maven build
        withMaven(mavenOpts: '--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.util.regex=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED') {
          sh "mvn clean package --show-version --batch-mode"
        }
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
