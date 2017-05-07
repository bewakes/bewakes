from django.contrib import admin
from blog.models import Article, Tag, ArticleImage
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
admin.site.register(Article, MarkdownModelAdmin)
admin.site.register(Tag)
admin.site.register(ArticleImage)
