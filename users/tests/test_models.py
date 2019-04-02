from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username='zoki',
            password='123testing',
            email='123@test.com'
        )
        self.assertEqual(user.username, 'zoki')
        self.assertEqual(user.email, '123@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.check_password('123testing'), True)

    def test_create_superuser(self):
        admin_user = get_user_model().objects.create_superuser(
            username='zoki',
            password='123testing',
            email='123@test.com'
        )
        self.assertEqual(admin_user.username, 'zoki')
        self.assertEqual(admin_user.email, '123@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.check_password('123testing'), True)
