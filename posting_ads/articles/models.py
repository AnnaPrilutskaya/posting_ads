from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')
    pub_date = models.DateField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        default=" ",
        related_name='author'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=" "
    )
    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE
    )
    comment = models.TextField('Комментарий')
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comment
