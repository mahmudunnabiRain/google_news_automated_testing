import time

from pages.top_stories_page import TopStoriesPage
from tests.base_test import BaseTest
from selenium import webdriver
import unittest


# test top stories
class TestCase003(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver')

    def test_3_3(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        page.get_headline_link().click()
        time.sleep(3)
        page.get_follow_button().click()
        time.sleep(3)
        if page.get_follow_window().is_displayed:
            print("follow window displayed")






