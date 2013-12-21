from fabric.operations import local, put, run, env, sudo, get
from fabric.context_managers import cd, lcd
from datetime import date

env.hosts = ['root@89.200.140.161']
env.password = 'fr3dalex'

def deploy():
    '''
    Live deploy to the server
    '''
    local('tar -cvjf jozi.tar.tbz -X exclude.txt ../jozi/')
    put('jozi.tar.tbz', '/srv/')
    run('rm -rf /srv/jozi/')
    with cd('/srv/'):
        run('tar -xvjf jozi.tar.tbz')
        run('rm jozi.tar.tbz')
        run('virtualenv jozi')
    with cd('/srv/jozi/'):
        run('/bin/bash -l -c "source bin/activate"')
        run('pip install -r requirements.txt')
        run('mv gunicorn_start.bash bin/')
        run('mv jozi/prod_settings.py jozi/settings.py')
        run('mkdir run/')
    sudo('service nginx restart')
    sudo('supervisorctl restart jozi')

def backup_data():
    rundate = date.strftime(date.today(), '%Y%m%d')
    with cd('/srv/pnsa_suites/'):
        run('pip install -r requirements.txt')
        run('./manage.py dumpdata --indent=3 > backup.{}'.format(rundate))
        run('tar -cjf backup.{0}.tbz backup.{0}'.format(rundate))
        run('rm backup.{}'.format(rundate))
        get('backup.{}.tbz'.format(rundate), 'backup.{}.tbz'.format(rundate))
        run('rm backup.{}.tbz'.format(rundate))

def reconfig():
    '''
    Automates web-server configuration changes
    ==========================================

    Copies up pnsa_suites.nginx -> nginx dir and restarts nginx
    Copies up pnsa_suites.conf -> supervisor dir and restarts supervisor
    '''
    put('pnsa_suites.nginx', '/etc/nginx/sites-available/pnsa_suites')
    sudo('service nginx restart')
    put('pnsa_suites.conf', '/etc/supervisor/conf.d/pnsa_suites.conf')
    sudo('supervisorctl restart pnsa_suites')

def deploy2test():
    '''
    Deploys to local /srv/ dir.  The local machine must be configured
    as live
    '''
    local('sudo rm -rf /srv/pnsa_suites/')
    local('tar -cvjf pnsa_suites.tar.gz -X exclude.txt ../pnsa_suites/')
    local('sudo mv pnsa_suites.tar.gz /srv/')
    with lcd('/srv/'):
        local('sudo tar -xvjf pnsa_suites.tar.gz')
        local('sudo virtualenv pnsa_suites')
    with lcd('/srv/pnsa_suites/'):
        local('/bin/bash -l -c "source bin/activate"')
        local('sudo pip install -r requirements.txt')
        local('sudo mv gunicorn_start.bash bin/')
        local('sudo mv suites/prod_settings.py suites/settings.py')
    local('sudo service nginx restart')
    local('sudo supervisorctl restart pnsa_suites')

