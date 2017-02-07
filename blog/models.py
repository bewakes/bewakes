import markdown
from django.db import models
from django_markdown.widgets import MarkdownWidget
from django_markdown.models import MarkdownField
from django.template.defaultfilters import slugify
from datetime import datetime

class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField('Tag')
    content = models.TextField()
    published_date = models.DateTimeField(default=datetime.now())
    slug = models.SlugField(blank=True)
    publish = models.BooleanField(default=True)
    visits = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            # newly created
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey('Article')
    comment_date = models.DateTimeField()
    username = models.CharField(max_length=75)
