import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryTest.settings')
app = Celery('celeryTest')

app.config_from_object('django.conf:settings', namespace='CELERY')

from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')