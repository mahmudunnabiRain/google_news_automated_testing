import time

from pages.top_stories_page import TopStoriesPage
from tests.base_test import BaseTest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pyperclip


# test top stories
class TestCase003(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver')
        self.wait = WebDriverWait(self.driver, 10)

    def test_3_1_1(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        page.click_headline_link()
        self.driver.implicitly_wait(3)
        page.click_follow_button()
        self.driver.implicitly_wait(3)
        if not page.get_sign_in_window().is_displayed:
            print("sign in window couldn't be displayed")

    def test_3_1_2_1(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        page.click_headline_link()
        self.driver.implicitly_wait(3)
        page.click_share_button()
        self.driver.implicitly_wait(3)
        page.click_copy_link()
        self.driver.implicitly_wait(3)
        self.driver.switch_to.new_window('tab')
        self.driver.get(pyperclip.paste())
        self.driver.implicitly_wait(3)
        self.assertEqual(page.get_headline_page_title().text, 'Headlines')

    def test_3_1_2_2(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        page.click_headline_link()
        self.driver.implicitly_wait(3)
        page.click_share_button()
        self.driver.implicitly_wait(3)
        original_window = self.driver.current_window_handle
        page.click_facebook_link()
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
            # Wait for the new tab to finish loading content
        self.wait.until(EC.title_is("Facebook"))

    def test_3_1_2_3(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        page.click_headline_link()
        self.driver.implicitly_wait(3)
        page.click_share_button()
        self.driver.implicitly_wait(3)
        original_window = self.driver.current_window_handle
        page.click_twitter_link()
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        self.wait.until(EC.title_is("Compose new Tweet / Twitter"))

    def test_3_2_1(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        news_title = page.get_any_news_title()

        # Performs mouse move action onto the element
        webdriver.ActionChains(self.driver).move_to_element(news_title).perform()
        self.driver.implicitly_wait(3)
        page.click_news_save_button()
        self.driver.implicitly_wait(3)
        if not page.get_sign_in_window().is_displayed:
            print("sign in window couldn't be displayed")

    def test_3_2_2_1(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        news_title = page.get_any_news_title()
        webdriver.ActionChains(self.driver).move_to_element(news_title).perform()
        self.driver.implicitly_wait(3)
        page.click_news_share_button()
        self.driver.implicitly_wait(3)
        page.click_copy_link()
        self.driver.implicitly_wait(3)
        link_site_name = page.get_share_pop_up_title().text
        self.driver.switch_to.new_window('tab')
        self.driver.get(pyperclip.paste())
        self.driver.implicitly_wait(3)
        self.assertIn(link_site_name, self.driver.page_source)

    def test_3_2_2_2(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        news_title = page.get_any_news_title()
        webdriver.ActionChains(self.driver).move_to_element(news_title).perform()
        self.driver.implicitly_wait(3)
        page.click_news_share_button()
        self.driver.implicitly_wait(3)
        original_window = self.driver.current_window_handle
        page.click_facebook_link()
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
            # Wait for the new tab to finish loading content
        self.wait.until(EC.title_is("Facebook"))

    def test_3_2_2_3(self):
        self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
        page = TopStoriesPage(self.driver)
        news_title = page.get_any_news_title()
        webdriver.ActionChains(self.driver).move_to_element(news_title).perform()
        self.driver.implicitly_wait(3)
        page.click_news_share_button()
        self.driver.implicitly_wait(3)
        original_window = self.driver.current_window_handle
        page.click_twitter_link()
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
            # Wait for the new tab to finish loading content
        self.wait.until(EC.title_is("Compose new Tweet / Twitter"))

    # def test_3_2_3_1(self):
    #     self.driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
    #     page = TopStoriesPage(self.driver)
    #     news_title = page.get_any_news_title()
    #     webdriver.ActionChains(self.driver).move_to_element(news_title).perform()
    #     self.driver.implicitly_wait(3)
    #     page.click_news_more_button()
    #     self.driver.implicitly_wait(3)
    #     page.click_view_full_coverage()

