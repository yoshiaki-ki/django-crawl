# coding: utf-8
from django.db.models import Q
import django_filters
from django.views import generic
from django.shortcuts import render
from .models import CompanyInfo, Article, Client, Tag


def index(request):
    return render(request, 'crawlApp/top.html/')


class CompanyInfoIndexView(generic.ListView):
    model = CompanyInfo
    paginate_by = 20

    def get_queryset(self):
        queryset = CompanyInfo.objects.order_by('company_name')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(company_name__icontains=keyword) | Q(category__icontains=keyword) | Q(address__icontains=keyword) | Q(
                    CEO__icontains=keyword) | Q(jojo__icontains=keyword) | Q(fund__icontains=keyword)
            )
        return queryset


class ArticleIndexView(generic.ListView):
    model = Article
    paginate_by = 20

    def get_queryset(self):
        queryset = Article.objects.order_by('-release_time')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword)
            )
        return queryset


class TagView(generic.ListView):
    paginate_by = 20
    model = Tag

    def base_queryset(self):
        queryset = Article.objects.all().order_by('-release_time')
        return queryset

    def get_queryset(self):
        tag = self.kwargs["tag"]
        queryset = self.base_queryset().filter(tag__name=tag)
        return queryset
