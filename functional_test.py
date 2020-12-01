from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Chrome(executable_path=r'C:\Users\acer\Downloads\chromedriver_win32\chromedriver.exe')
	def tearDown(self):
		self.browser.quit()
	def test_can_star_a_list_and_retrieve_it_lates(self):
		self.browser.get('http://localhost:8000')
		self.assertin('Todo',self.browser.title)
		self.fail('Finish the test!')
if __name__=='__main__':
	unittest.main(warnings='igore')