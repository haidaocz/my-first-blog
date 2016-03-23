# Register your models here.
from django.contrib import admin
from .models import Post, Comment, Article

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Article)