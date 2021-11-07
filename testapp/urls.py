from django.urls import path
from . import views

urlpatterns = [
    path('celery_test/', views.celery_test, name='celery_test'),
]

