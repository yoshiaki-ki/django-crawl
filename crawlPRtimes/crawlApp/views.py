# coding: utf-8

import django_filters
from django.views import generic
from django.shortcuts import render
from .models import CompanyInfo, Article, Client


class CompanyInfoIndexView(generic.ListView):
    model = CompanyInfo


class ArticleIndexView(generic.ListView):
    model = Article
