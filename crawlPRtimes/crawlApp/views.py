from django.shortcuts import render
from .models import CompanyInfo, Article, Client


# def index(request):
#     return render(request, 'index.html')


def index(request):
    articles = {
    "articles":Article.objects.all(),
    }
    return render(request, 'crawlApp/index.html', articles)


#
# company_name = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
# title = models.CharField(max_length=200)
# release_time = models.DateTimeField()
# is_technology = models.BooleanField(default=False)
# is_mobile = models.BooleanField(default=False)
# is_app = models.BooleanField(default=False)
# is_entertainment = models.BooleanField(default=False)
# is_beauty = models.BooleanField(default=False)
# is_fashion = models.BooleanField(default=False)
# is_lifestyle = models.BooleanField(default=False)
# is_business = models.BooleanField(default=False)
# is_gourmet = models.BooleanField(default=False)
# is_sports
