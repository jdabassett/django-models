from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack


class TestSnacksListView(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create_user(username="test_username", password="test_password", email="test_email")
        Snack.objects.create(name="test_name", description="test_description", purchaser=purchaser)

    def test_snack_list_status_code(self):
        response = self.client.get(reverse('snacks_list'))
        self.assertEqual(response.status_code, 200)

    def test_snack_list_templates(self):
        response = self.client.get(reverse('snacks_list'))
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_snack_list_contents(self):
        response = self.client.get(reverse('snacks_list'))
        response_html = response.content.decode('utf-8')
        self.assertContains(response, "test_name")
        self.assertContains(response, 'href="/1/"')
        self.assertEqual(response_html.count("test_name"), 1)

    def test_snack_detailed_status_code(self):
        response = self.client.get(reverse('snack_detailed', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_snack_detailed_templates(self):
        response = self.client.get(reverse('snack_detailed', args=(1,)))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'snack_detailed.html')

    def test_snack_detailed_contents(self):
        response = self.client.get(reverse('snack_detailed', args=(1,)))
        snack = response.context['snack_detailed']
        self.assertEqual(snack.name,'test_name')
        self.assertEqual(snack.description, 'test_description')
        self.assertEqual(snack.purchaser.username, 'test_username')
        




