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
        t.sleep(2)

class Speacial_Order(unittest.TestCase):
    def setup(self):
        self.options = Options()
        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_web(self):
        self.browser.get("http://127.0.0.1:8000/private/")
        t.sleep(2)
        '''
        Name of username is KRID
        KRID want to see question about doctor
        he's decide to go to http://127.0.0.1:8000/ using chrome browser
        and then UI ask him about what're you interested with?
        Krid saw that there are many options such as doctor, shopping, game
        and then Krid clicked on doctor 
        After than the website put Krid to private question that is about doctor only
        '''
        '''
        Another day Krid want to do something about shopping now
        so he decide to go to website again and now he choose about shopping
        and then website move Krid to private question again
        but now it's all about shopping as he want to
        '''
if __name__ == "__main__":
    unittest.main()