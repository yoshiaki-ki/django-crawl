# coding: utf-8

from rest_framework import serializers

from .models import CompanyInfo, Article, Client, Tag


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ('company_name', 'PRtimes_URL', 'official_URL', 'category',
                  'address', 'tel_number', 'CEO', 'jojo', 'fund', 'is_client')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('company_id', 'title', 'release_time', 'tag')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('company_name',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
