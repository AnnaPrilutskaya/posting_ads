from django.urls import path, include
#from articles.views import api_articles
#from articles.views import api_articles_detail
from rest_framework import routers 
from articles.views import ArticleViewSet, CommentViewSet
 
router = routers.DefaultRouter() 

router.register('articles', ArticleViewSet) 
router.register(r'articles/(?P<article_id>\d+)/comments', CommentViewSet) 

urlpatterns = [
    # Djoser автоматически создаст набор необходимых эндпоинтов.
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
    #path('articles/', api_articles),
    #path( 'articles/<int:pk>/', api_articles_detail )
    path('', include(router.urls)),
] 

