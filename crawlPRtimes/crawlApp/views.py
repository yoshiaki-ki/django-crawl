# coding: utf-8

import django_filters
from django.views import generic
from django.shortcuts import render
from .models import CompanyInfo, Article, Client


def index(request):
    return render(request, 'crawlApp/top.html/')


class CompanyInfoIndexView(generic.ListView):
    model = CompanyInfo
    paginate_by = 20


class ArticleIndexView(generic.ListView):
    model = Article
    paginate_by = 20
