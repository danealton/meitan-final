from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from news.models import News
from .views import ProductView, CategoryListView, CartRemove, CartAdd, filter_product, CartAddDetail, offer

urlpatterns = [
    url(r'^$', filter_product
        , name='product_list'),
    url(r'^(?P<slug>[^/]+)/$', ProductView.as_view()
        , name='products_detail'),
    url(r'^remove/(?P<product_id>\d+)/$', CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', CartAdd, name='CartAdd'),
    url(r'^adddetial/(?P<product_id>\d+)/$', CartAddDetail, name='CartAddDetail'),
    url(r'filter/$', filter_product, name='filter_product'),
]
