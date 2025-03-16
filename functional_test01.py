import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TestPoll(unittest.TestCase):

    def setUp(self):
        # ตั้งค่า options สำหรับ Chrome WebDriver
        self.options = Options()
        self.options.headless = False  # ตั้งค่าให้เบราว์เซอร์ไม่อยู่ในโหมด headless ถ้าต้องการให้เปิด UI
        
        # ใช้ WebDriverManager เพื่อดาวน์โหลด chromedriver และจัดการ path โดยอัตโนมัติ
        self.browser = webdriver.Chrome( options=self.options)
    
    def tearDown(self):
        # ปิดเบราว์เซอร์หลังการทดสอบ
        self.browser.quit()

    def test_can_start_web(self):
        # ทดสอบว่าเบราว์เซอร์สามารถเปิดหน้าเว็บที่ localhost ได้
        self.browser.get("http://127.0.0.1:8000/")
        
        # รอให้หน้าเว็บโหลดเสร็จ
        time.sleep(2)
        
        # ตรวจสอบว่า URL ปัจจุบันคือ localhost
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/")

if __name__ == "__main__":
    unittest.main()