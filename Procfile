web: gunicorn celeryTest.wsgi --log-file -
worker: celery worker -A celeryTest.celery -l INFO