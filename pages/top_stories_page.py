from selenium.webdriver.common.by import By
from locators.locators_top_stories_page import LocatorsTopStoriesPage


class TopStoriesPage:
    def __init__(self, driver):
        self.driver = driver

    def click_headline_link(self):
        self.driver.find_element(*LocatorsTopStoriesPage.HEADLINE_LINK).click()

    def click_follow_button(self):
        self.driver.find_element(*LocatorsTopStoriesPage.FOLLOW_BUTTON).click()

    def get_sign_in_window(self):
        return self.driver.find_element(*LocatorsTopStoriesPage.SIGN_IN_POP_UP)

    def click_share_button(self):
        self.driver.find_element(*LocatorsTopStoriesPage.SHARE_BUTTON).click()

    def get_share_pop_up_title(self):
        return self.driver.find_element(*LocatorsTopStoriesPage.SHARE_POP_UP_TITLE)

    def click_copy_link(self):
        self.driver.find_element(*LocatorsTopStoriesPage.COPY_LINK).click()

    def get_headline_page_title(self):
        return self.driver.find_element(*LocatorsTopStoriesPage.HEADLINE_PAGE_TITLE)

    def click_facebook_link(self):
        self.driver.find_element(*LocatorsTopStoriesPage.FACEBOOK_LINK).click()

    def click_twitter_link(self):
        self.driver.find_element(*LocatorsTopStoriesPage.TWITTER_LINK).click()

    def get_any_news_title(self):
        return self.driver.find_element(*LocatorsTopStoriesPage.NEWS_TITLE)

    def click_news_save_button(self):
        self.driver.find_element(*LocatorsTopStoriesPage.NEWS_SAVE_BUTTON).click()

    def click_news_share_button(self):
        self.driver.find_element(*LocatorsTopStoriesPage.NEWS_SHARE_BUTTON).click()

    def click_news_more_button(self):
        self.driver.find_element(*LocatorsTopStoriesPage.NEWS_MORE_BUTTON).click()

    def click_view_full_coverage(self):
        self.driver.find_element(*LocatorsTopStoriesPage.NEWS_VIEW_FULL_COVERAGE).click()