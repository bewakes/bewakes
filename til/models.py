from django.db import models
from blog.models import Tag

# Create your models here.

class TIL(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
