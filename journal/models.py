from django.db import models
import datetime

class Journal(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.created_date.strftime('%Y-%b-%d')
