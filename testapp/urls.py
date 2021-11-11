from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path("", views.index, name='index'),
    path('celery_test/', views.celery_test, name='celery_test'),
    path("boot/",views.boot,name="boot"),
    path("add/", views.adddiary, name="add"),
    path("ajax_test/", views.ajax_index,name="ajax_index"),
    path('ajax-number/', views.ajax_number, name='ajax_number'),
    path("setup/", views.setup, name="setup"),
    path("show_progress/", views.show_progress, name="show_progress"),
    path("do_something/", views.do_something, name="do_something"),
    path("show_status/", views.show_status, name="show_status"),
]

