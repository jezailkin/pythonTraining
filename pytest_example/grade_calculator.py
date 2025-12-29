import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class grade_calculator(unittest.TestCase):


    def setUp(self):
        self.base =baseSeleniumDalya()
        self.driver= self.base.selenium_start_with_url("https://www.calculator.net/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_clear(self):
        grade_calculator = self.driver.find_element(By.LINK_TEXT, "Grade Calculator")
        grade_calculator.click()

        homework = self.driver.find_element(By.NAME,"s1")
        homework.clear()
        homework.send_keys(50)
        Project = self.driver.find_element(By.NAME,"s2")
        Project.clear()
        Project.send_keys(55)
        Midterm_exam = self.driver.find_element(By.NAME,"s3")
        Midterm_exam.clear()
        Midterm_exam.send_keys(70)


        calculate = self.driver.find_element(By.NAME, "x")
        calculate.click()

        result = self. driver. find_element(By. CSS_SELECTOR, "p[class='verybigtext' ]")
        text = result. text
        index_1 = text.index(":") + 1
        index_2 = text.index("(") -1
        text = text[index_1:index_2].strip()
        print(text)
        text_float = float(text)
        print((text_float)+5)
