from django.contrib import admin
from . import models
# Register your models here.

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(models.Article)
admin.site.register(models.Comment)