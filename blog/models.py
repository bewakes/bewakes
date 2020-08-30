from django.db import models
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from datetime import datetime
import os


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField('Tag', related_name='articles')
    content = models.TextField()
    published_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(auto_now=True)
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


class ArticleImage(models.Model):
    image = models.ImageField()
    article = models.ForeignKey('Article')

    def __str__(self):
        return self.image.name


@receiver(models.signals.post_delete, sender=ArticleImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey('Article')
    comment_date = models.DateTimeField()
    username = models.CharField(max_length=75)


class HTMLJSItem(models.Model):
    # main file is index.html always
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=50)  # with respect to settings.HTMLJS_ROOT

    def __str__(self):
        return self.name

    @property
    def url(self):
        return "https://bewakes.com/htmljs/{}/index.html".format(self.path.strip('/'))
