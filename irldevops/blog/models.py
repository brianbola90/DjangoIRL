from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from meta.models import ModelMeta
import re
from irldevops.core.models import TimeStampModel
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField

# Create your models here.


class Post(ModelMeta, TimeStampModel):
    author = models.ForeignKey('users.User')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(_('slug'), max_length=50, populate_from=('title',))
    text = MarkdownxField()
    publish = models.BooleanField(default=False)

    tags = TaggableManager()

    _metadata = {
        'title': 'title',
        'author': 'author',
        'image': 'get_img_url'
    }

    class Meta:
        verbose_name_plural = "posts"

    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def create_meta_description(self):
        pass
        # TODO
        # description = self.text.split(' ')
        # word_list = description[0:10]
        # string = '\s'.join(e for e in word_list)
        # clean_description = re.sub('[^A-Za-z0-9\s]+', '', string45r)
        # return clean_description

    def get_img_url(self):
        regex = "\!\[.*\]\(([^)]+)"
        urls = re.findall(regex, self.text)
        if len(urls) > 0:
            return urls[0]
        else:
            return ""

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

    def __str__(self):
        return self.post.title
