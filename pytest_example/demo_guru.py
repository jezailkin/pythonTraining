import unittest

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class demo_guru(unittest.TestCase):

    def setUp(self):
        self.base=baseSeleniumDalya()
        self.driver=self.base.selenium_start_with_url("https://demo.guru99.com/test/newtours/reservation.php")

    def tearDown(self):
        self.base.selenium_stop()

