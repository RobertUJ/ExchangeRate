#!/bin/sh

echo "Start Project Exchange Rate"

echo "Make files for logs gunicorn and access logs"


mkdir /home/logs
touch /home/logs/gunicorn.log
touch /home/logs/access.log
tail -n 0 -f /home/logs/*.log &

echo "Go to dir project"
cd /code/ || exit

echo "Make Django migrations"
python manage.py migrate --noinput

echo "Create cache table"
python manage.py createcachetable

echo "Django collect statics --quiet"
# python manage.py collectstatic --noinput

echo "Starting app whit Gunicorn"

exec gunicorn -c gunicorn.conf.py exchangerate.wsgi:application \
     --name exchangerate \
     --log-level=info \
     --log-file=/home/logs/gunicorn.log \
     --access-logfile=/home/logs/access.log &

echo "Start Celery beat"
sleep 3

exec celery -A exchangerate worker -B --loglevel=INFO

echo "ExchangeRate Project Started"
