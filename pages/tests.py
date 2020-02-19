from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class HomePageTests(TestCase):
    credentials = {
        'username': 'testuser',
        'email': 'testuser@gmail.com',
        'password': 'pass1'
    }

    def test_signup_page_status_code(self):
        response = self.client.get('/users/new/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_by_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(**self.credentials)

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].username, self.credentials['username'])
        self.assertEqual(
            get_user_model().objects.all()[0].email, self.credentials['email']
        )

    def test_login_form(self):
        new_user = get_user_model().objects.create_user(**self.credentials)
        self.assertEqual(get_user_model().objects.all().count(), 1)

        response = self.client.post(
            '/users/login/', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)
        