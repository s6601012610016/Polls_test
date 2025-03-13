import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time as t

class TestPoll(unittest.TestCase):
    def setup(self):
        self.options = Options()
        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_web(self):
        self.browser.get("http://127.0.0.1:8000/")
        t.sleep(5)

if __name__ == "__main__":
    unittest.main()