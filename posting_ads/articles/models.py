from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

'''class User(AbstractUser):
    ADMIN = "admin"
    USER = "user"
    USER_ROLE = [
        ("user", USER),
        ("admin", ADMIN),
    ]

    username = models.CharField(
        "Логин",
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField(
        "Электронная почта",
        max_length=254,
        unique=True,
    )
    first_name = models.TextField(
        "Имя",
        max_length=150,
        blank=True
    )
    last_name = models.TextField(
        "Фамилия",
        max_length=150,
        blank=True
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_user(self):
        return self.role == self.USER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('username',)'''


class Articles(models.Model):
    title = models.CharField(max_length=16)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

class Comments(models.Model): 
    author = models.ForeignKey( 
        User, on_delete=models.CASCADE) 
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
    
