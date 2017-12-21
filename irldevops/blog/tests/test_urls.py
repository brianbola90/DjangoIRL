from django.core.urlresolvers import reverse, resolve
from test_plus.test import TestCase


class BlogTests(TestCase):

    def test_post_list(self):
        response = self.client.get('/blog/post/')
        self.assertEqual(response.status_code, 200)

    def test_list_reverse(self):
        """users:list should reverse to /users/."""
        self.assertEqual(reverse('blog:list'), '/blog/post/')

    def test_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve('/blog/post/').view_name, 'blog:list')
