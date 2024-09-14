from rest_framework import serializers
from .models import Articles, Comments


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True) 
    class Meta:
        fields = ('id', 'title', 'text', 'author', 'pub_date')
        model = Articles
        read_only_fields = ('author',)

class CommentSerializer(serializers.ModelSerializer): 
    author = serializers.StringRelatedField(read_only=True) 

    class Meta: 
        model = Comments
        fields = ('id', 'article', 'author', 'comment', 'pub_date') 
        read_only_fields = ('article', 'author',)