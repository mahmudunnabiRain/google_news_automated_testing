
from selenium.webdriver.common.by import By
from locators.locators_home_page import LocatorsHomePage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_search_box(self):
        return self.driver.find_element(*LocatorsHomePage.SEARCH_BOX)

    def get_featured_topic(self):
        return self.driver.find_element(*LocatorsHomePage.FEATURED_TOPIC)

    def get_in_the_news(self):
        return self.driver.find_element(*LocatorsHomePage.IN_THE_NEWS)

