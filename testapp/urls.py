from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path("", views.index, name='index'),
    path('celery_test/', views.celery_test, name='celery_test'),
    path("boot/",views.boot,name="boot"),
    path("add/", views.adddiary, name="add"),
]

