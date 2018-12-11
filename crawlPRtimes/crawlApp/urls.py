# coding: utf-8

from rest_framework import routers
# from .views import CompanyInfoViewSet, ArticleViewSet, ClientViewSet

from django.urls import path
from . import views

urlpatterns = [
    # path('articles', views.query, name='query'),
    path('', views.index, name='index'),
]
