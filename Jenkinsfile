node {

    // Scripted pipeline Version 2.0


        stage('Build') {
                echo 'Building..'
                checkout scm
               // build job: 'serverscripts'
        }
        stage('Test') {
                echo '*****************  Deploying to Testing environment.  *******************'
                sh 'scp server_upd.py erocha@test-crowd.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@test-jira.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@test-atldb.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@test-wiki.esc13.net:/home/erocha/bashscripts'

                sh 'ssh erocha@test-crowd.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'
                sh 'ssh erocha@test-jira.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'
                sh 'ssh erocha@test-atldb.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'
                sh 'ssh erocha@test-wiki.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'

                echo 'Deployment to Testing environment completed successfully...'
        }
        stage('Deploy') {
                echo '*****************  Deploying to Production environment.  *****************'
                sh 'scp server_upd.py erocha@crowd.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@jira.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@atldb.esc13.net:/home/erocha/bashscripts'
                sh 'scp server_upd.py erocha@wiki.esc13.net:/home/erocha/bashscripts' 

                sh 'ssh erocha@crowd.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'
                sh 'ssh erocha@jira.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'
                sh 'ssh erocha@atldb.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'
                sh 'ssh erocha@wiki.esc13.net chmod 755 /home/erocha/bashscripts/server_upd.py'


                echo 'Deployment to Production environment completed successfully!!!'
        }
}
