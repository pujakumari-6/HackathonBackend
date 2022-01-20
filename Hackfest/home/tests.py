from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


class PageTests(SimpleTestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTests(SimpleTestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class RegisterPageTests(SimpleTestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('registrationNo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'registrationNo.html')
