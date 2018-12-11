# coding: utf-8

from rest_framework import serializers

from .models import CompanyInfo, Article, Client


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ('company_name', 'PRtimes_URL','official_URL','category','address','tel_number','CEO','jojo','fund','is_client')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('company_name', 'title', 'release_time', 'is_technology', 'is_mobile','is_app','is_entertainment','is_beauty','is_fashion','is_lifestyle','is_business','is_gourmet','is_sports')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('company_name')
