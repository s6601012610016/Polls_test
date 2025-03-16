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

if __name__ == "__main__":
    unittest.main()
    