from django.db import models
from django.utils import timezone


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=100)
    PRtimes_URL = models.URLField()
    official_URL = models.URLField(null=True)
    category = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    tel_number = models.CharField(max_length=100, null=True)
    CEO = models.CharField(max_length=100, null=True)
    jojo = models.CharField(max_length=100, null=True)
    fund = models.CharField(max_length=100, null=True)
    is_client = models.BooleanField(default=False)

    def crawl_companyinfo(self):
        print("処理を実行しました")
        #企業情報クローリング処理を記載


class Tag(models.Model):
    name = models.CharField("タグ名", max_length=255)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return self.name

    # def get_latest_post(self):
    #     queryset = Article.objects.filter(tag=self)
    #     return _get_latest_post(queryset)


class Article(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    article_url = models.URLField(null=True)
    release_time = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="ジャンルタグ")


class Client(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
