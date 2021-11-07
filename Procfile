web: gunicorn celeryTest.wsgi --log-file -
worker: celery -A celeryTest.celery worker -l INFO