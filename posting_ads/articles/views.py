from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Articles, Comments
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import viewsets 
from django.shortcuts import get_object_or_404 
from .permissions import OwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer 
    permission_classes = (OwnerOrReadOnly,) 
    pagination_class = PageNumberPagination 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comments.objects.select_related('post')
    serializer_class = CommentSerializer 
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = PageNumberPagination 

    def get_queryset(self): 
        article_id = self.kwargs.get('article_id') 
        article = get_object_or_404(Articles, pk=article_id) 
        return Comments.objects.filter(article=article) 

    def perform_create(self, serializer): 
        article_id = self.kwargs.get('article_id') 
        article = get_object_or_404(Articles, pk=article_id) 
        serializer.save( 
            author=self.request.user, article=article 
        ) 
