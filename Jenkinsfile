pipeline {
   agent any
    environment {
      RELEASE='1.0.0'
      PROJECT_NAME='project-demo'
    }
   stages {
      stage('Audit tools') {
         steps{
            auditTools()
         }
      }
      stage('Build') {
            environment {
               MLRUN_DBPATH='https://mlrun-api.default-tenant.app.us-sales-341.iguazio-cd1.com'
               V3IO_ACCESS_KEY=credentials('V3IO_ACCESS_KEY')
               V3IO_USERNAME='xingsheng'
            }
            agent {
                docker {
                    image 'mlrun/mlrun:1.0.0'
                }
            }
            steps {
               echo "Building release ${RELEASE} for project ${PROJECT_NAME}..."
               sh 'chmod +x build.sh'
               withCredentials([string(credentialsId: 'an-api-key', variable: 'API_KEY')]) {
                  sh '''
                     ./build.sh
                  '''
               }
            }
        }
        stage('Test') {
            steps {
               echo "Testing release ${RELEASE}"
            }
        }
   }
   post {
      success {
         slackSend channel: '#builds',
                   color: 'good',
                   message: "Project ${env.PROJECT_NAME}, success: ${currentBuild.fullDisplayName}."
      }
      failure {
         slackSend channel: '#builds',
                   color: 'danger',
                   message: "Project ${env.PROJECT_NAME}, FAILED: ${currentBuild.fullDisplayName}."
      }
   }
}

void auditTools() {
   sh '''
      git version
      docker version
   '''
}