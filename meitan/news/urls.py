from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from news.models import News
from .views import NewsView


urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=News.objects.all(),
        ), name='news_list'),
    url(r'^(?P<slug>[^/]+)/$', NewsView.as_view()
        , name='news_detail'),
]
