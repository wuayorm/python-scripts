node {

    // Scripted pipeline Version 1.1
    // agent any


        stage('Build') {
                echo 'Building..'
                checkout scm
               // build job: 'serverscripts'
        }
        stage('Test') {
                echo 'Nothing to Test.'
        }
        stage('Deploy') {
                echo 'Deploying....'
                sh 'scp server_upd.py erocha@test-crowd.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@test-jira.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@test-atldb.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@test-wiki.esc13.net:/home/erocha/bashscripts'

                echo 'Deployment completed successfully!!!'
        }
}
