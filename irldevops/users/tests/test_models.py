from test_plus.test import TestCase
from blog.models import Post


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.post = Post.objects.create(title='title', text='body', author=self.user)

    def test__str__(self):
        self.assertEqual(
            self.post.__str__(),
            'title'
        )
