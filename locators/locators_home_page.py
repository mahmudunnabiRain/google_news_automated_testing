from selenium.webdriver.common.by import By


class LocatorsHomePage:
    SEARCH_BOX = (By.XPATH, "//input[@class='Ax4B8 ZAGvjd']")
    FEATURED_TOPIC = (By.XPATH, "//div[@class='MkjOTb oKubKe p1eHnf' and @data-hinttext='COVID-19']")
    IN_THE_NEWS = (By.XPATH, "//div[@class='MkjOTb oKubKe p1eHnf' and @data-hinttext='NFL']")
