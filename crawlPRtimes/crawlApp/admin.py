from django.contrib import admin
from .models import CompanyInfo, Article, Client, Tag

admin.site.register(CompanyInfo)
admin.site.register(Article)
admin.site.register(Client)
admin.site.register(Tag)
