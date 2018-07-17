import unittest
from selenium import webdriver


class StatusTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_is_operational(self):
        self.browser.get('http://localhost:5000/disneylife.globe.com.ph')
        self.assertIn('disneylife.globe.com.ph', self.browser.find_element_by_id("website").text)
        self.assertIn('Operational', self.browser.find_element_by_id("website_status").text)

    def test_is_major_outage(self):
        self.browser.get('http://localhost:5000/disneylife.globe.com.pha')
        self.assertIn('disneylife.globe.com.ph', self.browser.find_element_by_id("website").text)
        self.assertIn('Major Outage', self.browser.find_element_by_id("website_status").text)


if __name__ == '__main__':
    unittest.main()
