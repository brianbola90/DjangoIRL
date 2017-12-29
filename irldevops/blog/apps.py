from __future__ import unicode_literals

from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('post'))
        registry.register(self.get_model('comment'))
