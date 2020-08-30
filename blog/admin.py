from django.contrib import admin
from blog.models import Article, Tag, ArticleImage, HTMLJSItem

# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(ArticleImage)
admin.site.register(HTMLJSItem)
