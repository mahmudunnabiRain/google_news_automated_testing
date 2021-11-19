from selenium.webdriver.common.by import By


class LocatorsTopStoriesPage:
    HEADLINE_LINK = (By.XPATH, "//a[@class='wmzpFf  yETrXb Ir3o3e ndj7Ed']")

    FOLLOW_BUTTON = (By.XPATH, "//div[@class='OGsJDe']")
    SIGN_IN_POP_UP = (By.XPATH, "//div[@class='VfPpkd-P5QLlc']")

    SHARE_BUTTON = (By.XPATH, "//div[@class='MSFRuc Q3T0Df']")
    COPY_LINK = (By.XPATH, "//div[@class='UI9lcc' and @jsname='link']")
    FACEBOOK_LINK = (By.XPATH, "//div[@class='UI9lcc' and @jsname='facebook']")
    TWITTER_LINK = (By.XPATH, "//div[@class='UI9lcc' and @jsname='twitter']")

    HEADLINE_PAGE_TITLE = (By.XPATH, "//h2[@class='OJMBqe']")

    NEWS_TITLE = (By.XPATH, "//a[@class='VDXfz']")
    NEWS_SAVE_BUTTON = (By.XPATH, "//div[@class='OGsJDe L8PZAb R71ogd']")
    NEWS_SHARE_BUTTON = (By.XPATH, "//span[@class='L8PZAb uG2FLd']")
    NEWS_MORE_BUTTON = (By.XPATH, "//span[@class=' L8PZAb GB1Zid']")
    NEWS_VIEW_FULL_COVERAGE = (By.XPATH, "//span[@class='z80M1' and @aria-label='View Full coverage']")

    SHARE_POP_UP_TITLE = (By.XPATH, "//div[@class='yvOtgc']")
