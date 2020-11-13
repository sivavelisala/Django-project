from django.db import models
from django.utils import timezone
# Create your models here.


class Posts(models.Model):

    author = models.TextField(max_length=100)
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(default=timezone.now)
