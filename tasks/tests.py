from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TaskFlowPagesTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='demo',
            email='demo@example.com',
            password='StrongPass123!'
        )

    def test_categories_page_is_accessible(self):
        self.client.login(username='demo', password='StrongPass123!')
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page_is_accessible(self):
        self.client.login(username='demo', password='StrongPass123!')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_is_accessible(self):
        self.client.login(username='demo', password='StrongPass123!')
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
