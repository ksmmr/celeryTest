web: gunicorn celeryTest.wsgi --log-file -
worker: celery worker --app=celeryTest.celery -l INFO