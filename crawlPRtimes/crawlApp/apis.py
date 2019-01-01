from rest_framework import viewsets, filters, routers
from .models import CompanyInfo, Article, Client, Tag
from .serializer import CompanyInfoSerializer, ArticleSerializer, ClientSerializer, TagSerializer


class CompanyInfoViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

router = routers.DefaultRouter()
router.register(r'company_info', CompanyInfoViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'client', ClientViewSet)
router.register(r'tag', TagViewSet)
