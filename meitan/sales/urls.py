from django.conf.urls import include, url
from .views import offer

urlpatterns = [
    url(r'offer/$', offer, name='offer'),
]
