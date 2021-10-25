from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class waitUtils:
    def __init__(self, driver):
        self.driver = driver

    def waitForElementPresence(self, elementXpath):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, elementXpath)))

    def waitTillUrlContains(self, urlData):
        WebDriverWait(self.driver, 30).until(expected_conditions.url_contains(urlData))