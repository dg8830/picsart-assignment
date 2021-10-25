from selenium.webdriver.common.by import By
from utils.waitUtils import waitUtils


class loginOutPage:
    LOGOUT_ROOT = "//div[contains(@class,'drop-down profile')]"

    def __init__(self, driver):
        self.driver = driver

    def logoutUser(self):
        self.driver.find_element(By.XPATH, self.LOGOUT_ROOT + "//a[@data-test='logout-button']").click()
        waitUtils.waitForElementPresence(self, "//button[@data-test='login-button']")
