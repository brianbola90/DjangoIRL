from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from actstream.models import following, followers
import hashlib
from allauth.socialaccount.models import SocialAccount



@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    bio = models.TextField(blank=True, max_length=1000)

    def profile_image_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "https://api.adorable.io/avatars/150/{}.png?s=100".format(
            hashlib.md5(self.email).hexdigest())

    def profile_image_url_thumb(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "https://api.adorable.io/avatars/50/{}.png?s=100".format(
            hashlib.md5(self.email).hexdigest())

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_followers_list(self):
        return followers(self)

    def get_following_list(self):
        return following(self)

    def get_followers_count(self):
        return len(followers(self))

    def get_following_count(self):
        return len(following(self))

