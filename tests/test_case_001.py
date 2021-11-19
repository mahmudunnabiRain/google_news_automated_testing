from pages.home_page import HomePage
from tests.base_test import BaseTest
from selenium import webdriver
import unittest


# test website
class TestCase001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver')

    def test(self):
        # test case 001
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        assert "Google News" == self.driver.title
