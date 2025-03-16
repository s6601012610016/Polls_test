import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestPoll(unittest.TestCase):

    def setUp(self):
        # ตั้งค่า options สำหรับ Chrome WebDriver
        self.options = Options()
        self.options.headless = False  # ตั้งค่าให้เบราว์เซอร์ไม่อยู่ในโหมด headless ถ้าต้องการให้เปิด UI
        
        # เปิด Chrome browser
        self.browser = webdriver.Chrome(options=self.options)
    
    def tearDown(self):
        # ปิดเบราว์เซอร์หลังการทดสอบ
        self.browser.quit()

    def test_vote_for_question_with_text(self):
        # 1. ไปที่หน้าเว็บที่แสดงคำถามทั้งหมด
        self.browser.get("http://127.0.0.1:8000/")
        
        # รอจนกว่าจะสามารถค้นหาคำถามทั้งหมดได้
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li a"))
        )
        time.sleep(2)  # เว้นเวลา 2 วินาที
        
        # ค้นหาคำถามทั้งหมด
        question_links = self.browser.find_elements(By.CSS_SELECTOR, "li a")
        print(f"Number of questions: {len(question_links)}")  # แสดงจำนวนคำถามทั้งหมด
        
        # ค้นหาคำถามที่มีข้อความ 'this is WARM'
        question_to_vote = None
        for question_link in question_links:
            if "this is WARM" in question_link.text:
                question_to_vote = question_link
                break
        
        # ตรวจสอบว่าเจอคำถามที่ต้องการหรือไม่
        if question_to_vote:
            # 2. คลิกคำถามที่มีข้อความ 'this is WARM'
            question_to_vote.click()

            # รอให้หน้าเว็บคำถามโหลด
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='radio']"))
            )
            time.sleep(2)  # เว้นเวลา 2 วินาที
            
            # 3. โหวตตัวเลือกแรกในคำถาม
            choice_buttons = self.browser.find_elements(By.CSS_SELECTOR, "input[type='radio']")  # สมมติว่าแต่ละตัวเลือกเป็น input[type='radio']
            if choice_buttons:
                choice_buttons[0].click()  # โหวตตัวเลือกแรก (index 0)
                time.sleep(2)  # เว้นเวลา 2 วินาที

                # 4. กดปุ่ม Submit
                submit_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
                submit_button.click()
                
                # รอให้หน้าเว็บผลโหวตโหลด
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                )
                time.sleep(2)  # เว้นเวลา 2 วินาที

                # 5. ตรวจสอบว่าผลโหวตแสดงผล
                self.assertIn("results", self.browser.current_url)  # ตรวจสอบว่า URL มี "results"
                
                # 6. คลิกที่ลิงก์ "Back to homepage" เพื่อกลับไปหน้าหลัก
                back_to_homepage_link = self.browser.find_element(By.LINK_TEXT, "Back to homepage")
                back_to_homepage_link.click()

                # รอให้หน้าหลักโหลด
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li a"))
                )
                time.sleep(2)  # เว้นเวลา 2 วินาที

                # 7. ตรวจสอบว่าเราอยู่ที่หน้าหลักแล้ว
                self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/")

                # ค้นหาคำถามทั้งหมดใหม่ หลังจากกลับมาที่หน้าหลัก
                question_links = self.browser.find_elements(By.CSS_SELECTOR, "li a")

                # 8. ไปที่คำถามที่มีข้อความ "this is HOT"
                question_to_vote_hot = None
                for question_link in question_links:
                    if "this is HOT" in question_link.text:
                        question_to_vote_hot = question_link
                        break
                
                # ตรวจสอบว่าเจอคำถามที่มีข้อความ "this is HOT"
                if question_to_vote_hot:
                    # 9. คลิกคำถามที่มีข้อความ 'this is HOT'
                    question_to_vote_hot.click()

                    # รอให้หน้าเว็บคำถามโหลด
                    WebDriverWait(self.browser, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='radio']"))
                    )
                    time.sleep(2)  # เว้นเวลา 2 วินาที
                    
                    # 10. โหวตตัวเลือกแรกในคำถาม
                    choice_buttons = self.browser.find_elements(By.CSS_SELECTOR, "input[type='radio']")
                    if choice_buttons:
                        choice_buttons[0].click()  # โหวตตัวเลือกแรก (index 0)
                        time.sleep(2)  # เว้นเวลา 2 วินาที

                        # 11. กดปุ่ม Submit
                        submit_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
                        submit_button.click()
                        
                        # รอให้หน้าเว็บผลโหวตโหลด
                        WebDriverWait(self.browser, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                        )
                        time.sleep(2)  # เว้นเวลา 2 วินาที

                        # 12. ตรวจสอบว่าผลโหวตแสดงผล
                        self.assertIn("results", self.browser.current_url)  # ตรวจสอบว่า URL มี "results"
                        
                        # 13. คลิกที่ลิงก์ "Back to homepage" เพื่อกลับไปหน้าหลัก
                        back_to_homepage_link = self.browser.find_element(By.LINK_TEXT, "Back to homepage")
                        back_to_homepage_link.click()

                        # รอให้หน้าหลักโหลด
                        WebDriverWait(self.browser, 10).until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li a"))
                        )
                        time.sleep(2)  # เว้นเวลา 2 วินาที

                        # 14. ตรวจสอบว่าเราอยู่ที่หน้าหลักแล้ว
                        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/")
                else:
                    self.fail("ไม่พบคำถามที่มีข้อความ 'this is HOT'")

            else:
                self.fail("ไม่พบตัวเลือกให้โหวตในคำถาม")
        else:
            self.fail("ไม่พบคำถามที่มีข้อความ 'this is WARM'")

if __name__ == "__main__":
    unittest.main()
