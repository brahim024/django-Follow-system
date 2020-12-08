from django.test import TestCase
from list.views import index
# Create your tests here.
'''class HomePagetest(TestCase):
	def test_view_url_exists_at_desired_location(self):
    	response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
'''
class SmokeTest(TestCase):
	def test_bad(self):
		self.assertEqual(1+1,2)