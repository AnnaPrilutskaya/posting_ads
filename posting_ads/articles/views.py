from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Articles, Comments
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import viewsets 
from .permissions import IsAuthorOrReadOnlyPermission
from django.shortcuts import get_object_or_404 


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer 
    permission_classes = (IsAuthorOrReadOnlyPermission,) 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comments.objects.select_related('post')
    serializer_class = CommentSerializer 
    permission_classes = (IsAuthorOrReadOnlyPermission,)

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



'''@api_view(['GET', 'POST'])
def api_articles(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    posts = Articles.objects.all()
    serializer = ArticleSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_articles_detail(request, pk):
    post = Articles.objects.get(id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = ArticleSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ArticleSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)'''