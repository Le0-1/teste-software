from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):
    def setUp(self):
        self.list_url = reverse('list')  # substitua 'list' pelo nome da sua URL
        self.detail_url = reverse('detail', args=['some-arg'])  # substitua 'detail' e 'some-arg' conforme necessário
        self.project1 =  Project.objects.create(
            name='some-arg',
            budget=10000
        )

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')