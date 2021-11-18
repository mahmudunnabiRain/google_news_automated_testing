
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_search_box(self):
        return self.driver.find_element(By.XPATH, "//input[@class='Ax4B8 ZAGvjd']")

    def get_featured_topic(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MkjOTb oKubKe p1eHnf' and @data-hinttext='COVID-19']")

    def get_in_the_news(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MkjOTb oKubKe p1eHnf' and @data-hinttext='NFL']")

