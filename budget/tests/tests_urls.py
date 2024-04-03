from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):

    def test_url_list_is_resolves(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, project_list)
    pass

    def test_add_url_resolves(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.view_class , ProjectCreateView)
    pass

    def test_detail_url_resolves(self):
        url = reverse('detail', args=['some-slug'])
        self.assertEqual(resolve(url).func, project_detail)
    pass