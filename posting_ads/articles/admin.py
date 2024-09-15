from django.contrib import admin
from .models import Articles, Comments


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    search_fields = ('title',)
    list_filter = ('pub_date',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'pub_date')
    search_fields = ('comment',)
    list_filter = ('pub_date',)


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comments, CommentsAdmin)
