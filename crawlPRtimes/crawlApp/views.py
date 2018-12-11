# coding: utf-8

import django_filters
from django.shortcuts import render
from .models import CompanyInfo, Article, Client


# def index(request):
#     return render(request, 'index.html')


def index(request):
    articles = {
        "articles" : Article.objects.all(),
    }
    return render(request, 'crawlApp/index.html', articles)
