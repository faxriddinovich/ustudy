from django.contrib.auth.models import User
from django.test import TestCase

from post.models import Post


# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUp(cls):
        admin_user = User.objects.create_superuser(username='admin', password='admin@123456')
        admin_user.save()
        test_post = Post.objects.create(title='Test Post', content='Test Content', author=admin_user)
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        content = f'{post.content}'
        title = f'{post.title}'
        self.assertEqual(author, 'admin')
        self.assertEqual(content, 'Test Content')
        self.assertEqual(title, 'Test Post')

        #yaratilgan api endpointlar uchun test yozildi va run qilindi...
