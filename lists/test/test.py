from django.test import TestCase
from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Chrome(executable_path=r'C:\Users\acer\Downloads\chromedriver_win32\chromedriver.exe')
	def tearDown(self):
		self.browser.quit()
	def test_can_star_a_list_and_retrieve_it_lates(self):
		self.browser.get('http://localhost:8000')
		#self.browser.implicitly_wait(3)
		self.asserting('Todo',self.browser.title)
		print(self.fail('Finish the test!'))

if __name__=='__main__':
	unittest.main(warnings='ignore')