from django.shortcuts import render
from django.http import HttpResponse
from feincms.module.page.models import Page
from django.utils.translation import get_language
from django.http import JsonResponse
from .utils import pages_to_dict


def pages_json(request):
    pages = Page.objects.filter(level=0, language=get_language(), in_navigation=True)
    # print pages
    return JsonResponse(pages_to_dict(pages), safe=False)
