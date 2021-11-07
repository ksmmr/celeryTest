web: gunicorn celeryTest.wsgi --log-file -
worker: celery worker --app=tasks.app