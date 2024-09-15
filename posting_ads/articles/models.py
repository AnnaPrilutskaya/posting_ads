from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Articles(models.Model):
    title = models.CharField(max_length=16)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = " ", related_name='author')

    class Meta: 
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

class Comments(models.Model): 
    author = models.ForeignKey( 
        User, on_delete=models.CASCADE, default = " ") 
    article = models.ForeignKey( 
        Articles, on_delete=models.CASCADE) 
    comment = models.TextField() 
    pub_date = models.DateTimeField( 
        'Дата добавления', auto_now_add=True, db_index=True 
    ) 
    class Meta: 
        ordering = ['-pub_date'] 
 
    def __str__(self): 
        return self.comment
    
