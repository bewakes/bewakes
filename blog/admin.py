from django.contrib import admin
from blog.models import Article, Tag
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
admin.site.register(Article, MarkdownModelAdmin)
admin.site.register(Tag)
