import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from private.models import Question

def create_question(question_text, days):
    """
    สร้างคำถามในฐานข้อมูลของแอป private
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):

    def test_three_questions_displayed(self):
        """
        ทดสอบว่าในหน้า index ของแอป private จะมีคำถามทั้งหมด 3 คำถามแสดง
        """
        # สร้างคำถาม 3 คำถามในฐานข้อมูล
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        question3 = create_question(question_text="Past question 3.", days=-1)

        # เรียกดูหน้า index ของแอป private
        response = self.client.get(reverse("private:index"))  # ใช้ URL ของแอป private

        # ตรวจสอบว่ามีคำถามทั้งหมด 3 คำถามแสดงในหน้า index
        self.assertContains(response, question1.question_text)
        self.assertContains(response, question2.question_text)
        self.assertContains(response, question3.question_text)

        # ตรวจสอบว่าใน context มีคำถาม 3 คำถาม
        self.assertEqual(len(response.context["latest_question_list"]), 3)

    def test_less_than_three_questions(self):
        """
        ถ้ามีคำถามน้อยกว่า 3 คำถาม จะต้องแสดงคำถามทั้งหมดที่มีในฐานข้อมูล
        """
        # สร้างคำถาม 2 คำถามในฐานข้อมูล
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)

        # เรียกดูหน้า index ของแอป private
        response = self.client.get(reverse("private:index"))

        # ตรวจสอบว่ามีคำถาม 2 คำถามแสดงในหน้า index
        self.assertContains(response, question1.question_text)
        self.assertContains(response, question2.question_text)

        # ตรวจสอบว่าใน context มีคำถาม 2 คำถาม
        self.assertEqual(len(response.context["latest_question_list"]), 2)
