from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from irldevops.core.models import TimeStampModel
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.


class Post(TimeStampModel):
    author = models.ForeignKey('users.User')
    title = models.CharField(max_length=200)
    text = MarkdownxField()
    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "posts"

    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def publish_post(self):
        self.publish = True
        self.save()


class Comment(TimeStampModel):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('users.User')
    text = models.TextField()
    approved_comment = models.BooleanField(default=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def approve(self):
        self.approved_comment = True
        self.save()

    def unapprove(self):
        self.approved_comment = False
        self.save()
