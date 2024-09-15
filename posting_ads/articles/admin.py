from django.contrib import admin
from .models import Articles, Comments
from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.admin import UserAdmin

admin.site.register(Articles)
admin.site.register(Comments)


