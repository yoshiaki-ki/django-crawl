from django.db import models
from django.utils import timezone


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=30)
    PRtimes_URL = models.URLField()
    official_URL = models.URLField()
    category = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    tel_number = models.IntegerField()
    CEO = models.CharField(max_length=20)
    jojo = models.CharField(max_length=20)
    fund = models.CharField(max_length=20)
    is_client = models.BooleanField(default=False)


class Article(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    release_time = models.DateTimeField()
    is_technology = models.BooleanField(default=False)
    is_mobile = models.BooleanField(default=False)
    is_app = models.BooleanField(default=False)
    is_entertainment = models.BooleanField(default=False)
    is_beauty = models.BooleanField(default=False)
    is_fashion = models.BooleanField(default=False)
    is_lifestyle = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    is_gourmet = models.BooleanField(default=False)
    is_sports = models.BooleanField(default=False)


class Client(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
