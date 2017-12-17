from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampModel

# Create your models here.


class Post(TimeStampModel):
    author = models.ForeignKey('users.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title


class Comment(TimeStampModel):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=True)
