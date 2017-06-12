from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import News, NewsImage


# Create your views here.
class NewsView(DetailView):
    model = News
    #template_name = 'agenda/agenda_gallery.html'


    def get_queryset(self):
        return News.objects.filter(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        active_news = News.objects.get(slug=self.kwargs.get('slug'))

        context = super(NewsView, self).get_context_data(**kwargs)
        context["images"] = NewsImage.objects.filter(news_id=int(active_news.id))
        return context
