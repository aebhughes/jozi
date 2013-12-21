#!/bin/bash
 
NAME="jozi_app"
DJANGODIR=/srv/jozi
SOCKFILE=/srv/jozi/run/gunicorn.sock
USER=root
GROUP=root
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=jozi.settings
DJANGO_WSGI_MODULE=jozi.wsgi
 
echo "Starting $NAME"
 
# Activate the virtual environment
cd $DJANGODIR
source bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE
