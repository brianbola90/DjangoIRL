from django.core.urlresolvers import reverse, resolve
from test_plus.test import TestCase
from blog.models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.post = Post.objects.create(title='1-title', text='1-body', author=self.user)

    def test_post_list(self):
        response = self.client.get('/blog/post/')
        self.assertEqual(response.status_code, 200)

    def test_list_reverse(self):
        """blog:list should reverse to /blog/post/."""
        self.assertEqual(reverse('blog:list'), '/blog/post/')

    def test_list_resolve(self):
        """/blog/post/ should resolve to blog:list."""
        self.assertEqual(resolve('/blog/post/').view_name, 'blog:list')

    def test_detail_resolve(self):
        """blog/post/1 should resolve to blog:detail"""
        self.assertEqual(
            resolve('/blog/post/1').view_name, 'blog:detail'
        )

    def test_detail_reverse(self):
        """blog:detail should resolve to /blog/post/1"""
        self.assertEqual(
            reverse('blog:detail', kwargs={'pk': 1}),
            '/blog/post/1'
        )

    def tearDown(self):
        del self.post
        del self.user
