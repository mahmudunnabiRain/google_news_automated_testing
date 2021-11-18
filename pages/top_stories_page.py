from selenium.webdriver.common.by import By


class TopStoriesPage:
    def __init__(self, driver):
        self.driver = driver

    def get_headline_link(self):
        return self.driver.find_element(By.XPATH, "//a[@class='wmzpFf  yETrXb Ir3o3e ndj7Ed']")

    def get_follow_button(self):
        return self.driver.find_element(By.XPATH, "//div[@class='OGsJDe']")

    def get_follow_window(self):
        return self.driver.find_element(By.XPATH, "//div[@class='VfPpkd-P5QLlc']")
