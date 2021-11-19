import time

from pages.home_page import HomePage
from tests.base_test import BaseTest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# test search
class TestCase002(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver')

    def test_2_1(self):
        # test case 002.1
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = HomePage(self.driver)
        page.get_search_box().click()
        self.driver.implicitly_wait(3)
        topic = page.get_featured_topic()
        topic_name = topic.text
        topic.click()
        self.driver.implicitly_wait(3)
        assert topic_name in self.driver.find_element(By.XPATH, "//h2[@class='OJMBqe']").text

    def test_2_2(self):
        # test case 002.2
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = HomePage(self.driver)
        page.get_search_box().click()
        self.driver.implicitly_wait(3)
        topic = page.get_in_the_news()
        topic.click()
        self.driver.implicitly_wait(3)

