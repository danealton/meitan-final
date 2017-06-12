from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^api/pages/$', views.pages_json, name='api-pages'),
]
