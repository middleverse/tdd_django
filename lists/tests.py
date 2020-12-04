from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
# from lists.views import about_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
   
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request) # returns HttpResponse object
        html = response.content.decode('utf8') # response content is in binary and need to be decoded 
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>TODO Lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
