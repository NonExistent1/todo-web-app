"""
    Jordyn Kuhn
    CIS 218
    1/30/2024
"""

from django.test import TestCase
from django.urls import reverse

from .models import Todo

class TodoTests(TestCase):
    """Todo Tests"""

    @classmethod
    def setUpTestData(cls):
        """Set up the data needed for each test"""
        cls.post = Todo.objects.create(text = "This is a test!", complete_by = "2000-1-1 12:00:00")

    def test_model_content(self):
        """Test the model content"""
        self.assertEqual(self.post.text, "This is a test!")
        self.assertEqual(self.post.complete_by, "2000-1-1 12:00:00")

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test the home page"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")
        self.assertContains(response, "Jan. 1, 2000, noon")