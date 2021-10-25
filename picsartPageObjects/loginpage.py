from selenium.webdriver.common.by import By
from utils.waitUtils import waitUtils


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        waitUtils.waitForElementPresence(self, "//button[contains(@class,'createButton')]")
        waitUtils.waitForElementPresence(self, "//picture")
        return self.driver.find_element(By.XPATH,"//picture")
