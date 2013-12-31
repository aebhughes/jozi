from fabric.operations import local, put, run, env, sudo, get
from fabric.context_managers import cd, lcd
from datetime import date

env.hosts = ['root@89.200.140.161']
env.password = 'fr3dalex'

def deploy():
    '''
    Live deploy to the server
    '''
    local('tar -cvzf jozi.tbz -X exclude.txt ../jozi/')
    put('jozi.tbz', '/srv/')
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
    with cd('/srv/jozi/'):
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

    Copies up jozi.nginx -> nginx dir and restarts nginx
    Copies up jozi.conf -> supervisor dir and restarts supervisor
    '''
    put('jozi.nginx', '/etc/nginx/sites-available/jozi')
    sudo('service nginx restart')
    put('jozi.conf', '/etc/supervisor/conf.d/jozi.conf')
    sudo('supervisorctl restart jozi')
