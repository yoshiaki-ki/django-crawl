# coding: utf-8

from rest_framework import routers
# from .views import CompanyInfoViewSet, ArticleViewSet, ClientViewSet
from django.views import generic
from django.urls import path
from . import views

urlpatterns = [
    # path('articles', views.query, name='query'),
    path('', views.index, name='top'),
    path('company', views.CompanyInfoIndexView.as_view(), name='companyinfo_list'),
    path('article', views.ArticleIndexView.as_view(), name='article_list'),
]
