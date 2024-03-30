from django.test import TestCase, RequestFactory
from django.template import Context, Template
from django.urls import reverse

from .models import MenuItem
# Create your tests here.


class MenuTestCase(TestCase):
    fixtures = [
        "items.json",
        "menu.json"
    ]

    def setUp(self):
        """
            Creating RequestFactory for generating context and request
        """
        self.req_factory = RequestFactory()
        self.request = self.req_factory.get(reverse('home'))
    
    def test_one_query(self):
        """
            Checking, there is one query to render one menu
        """
        with self.assertNumQueries(1):
            context = Context({'request': self.request})
            template = Template("{% load menu_tags %}{% draw_menu 'menu1' %}")
            template.render(context)
