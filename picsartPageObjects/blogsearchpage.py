from selenium.webdriver.common.by import By
from utils.waitUtils import waitUtils


class blogSearchPage:
    SEARCH_FORM_ROOT = "//div[contains(@class,'search-form-root')]"
    SEARCH_BUTTON = SEARCH_FORM_ROOT + "//button[contains(@class,'searchButton')]"
    SEARCH_RESULTS = "//div[@data-watermark='search']"
    COOKIE_POPUP = "//button[@id='onetrust-accept-btn-handler']"

    def __init__(self, driver):
        self.driver = driver

    def search(self, text):
        waitUtils.waitForElementPresence(self, self.COOKIE_POPUP)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        waitUtils.waitForElementPresence(self, self.SEARCH_BUTTON)
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON + "//*[name()='svg']").click()
        waitUtils.waitForElementPresence(self, "//input[@name='search']")
        self.driver.find_element(By.NAME,"search").send_keys(text)
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON + "//*[name()='svg']").click()
        waitUtils.waitForElementPresence(self, self.SEARCH_RESULTS+"/div")
        waitUtils.waitTillUrlContains(self, text)
        return self.driver.find_element(By.XPATH, self.SEARCH_RESULTS + "/h2").text