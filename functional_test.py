import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TestPrivatePolls(unittest.TestCase):

    def setUp(self):
        # ตั้งค่า options สำหรับ Chrome WebDriver
        self.options = Options()
        self.options.headless = False  # ตั้งค่าให้เบราว์เซอร์ไม่อยู่ในโหมด headless ถ้าต้องการให้เปิด UI
        
        # เปิด Chrome browser
        self.browser = webdriver.Chrome(options=self.options)
    
    def tearDown(self):
        # ปิดเบราว์เซอร์หลังการทดสอบ
        self.browser.quit()

    def test_go_to_private_polls(self):
        # 1. ไปที่หน้าเว็บที่แสดงคำถามทั้งหมด
        self.browser.get("http://127.0.0.1:8000/")
        time.sleep(2)  # เว้นเวลา 2 วินาที
        
        # 2. คลิกที่ลิงก์ "Go to Private Polls"
        private_poll_link = self.browser.find_element(By.LINK_TEXT, "Go to Private Polls")
        private_poll_link.click()
        time.sleep(2)  # เว้นเวลา 2 วินาที
        
        # 3. ตรวจสอบว่าเราอยู่ในหน้า Private Polls
        self.assertIn("private", self.browser.current_url)
        time.sleep(2)  # เว้นเวลา 2 วินาที

    def test_special_order(self):
        pass
        #self.browser.get("http://127.0.0.1:8000/private/")
        #t.sleep(2)
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
    