from selenium.webdriver.common.by import By
from utils.waitUtils import waitUtils


class homePage:
    HEADER_ROOT = "//div[contains(@class,'content-root')]"

    def __init__(self, driver):
        self.driver = driver

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,"//button[@data-test='login-button']").click()
        waitUtils.waitForElementPresence(self, "//input[@name='username']")

    def clickLogo(self):
        self.driver.find_element(By.XPATH,self.HEADER_ROOT + "/div[contains(@class,'logo')]/a").click()
        if len(self.driver.find_elements(By.XPATH,"//button[@data-test='login-button']")) >0:
            waitUtils.waitForElementPresence(self, "//span[text()='Start Editing']/parent::a")