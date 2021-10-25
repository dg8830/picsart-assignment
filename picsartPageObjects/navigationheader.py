from selenium.webdriver.common.by import By
from utils.waitUtils import waitUtils


class navigationHeaderPage:
    NAVIGATION_ROOT = "//header//nav[contains(@class,'header-dev-navigation-root')]"
    DROP_DOWN_NAVIGATION_ROOT = "//div[contains(@class,'drop-down navigation')]"
    BLOG_HEADER_ROOT = "//div[contains(@class,'layout-header')]"
    BLOG_NAVIGATION_LIST = BLOG_HEADER_ROOT + "//ul[contains(@class,'navigation-navList')]"
    LOADING_ROOT = "//div[contains(@class,'loading-root')]"
    LOADING_ICON = LOADING_ROOT + "//*[name()='svg']"

    def __init__(self, driver):
        self.driver = driver

    def clickLearn(self):
        self.driver.find_element(By.XPATH, self.NAVIGATION_ROOT + "//strong[text()='Learn']").click()
        waitUtils.waitForElementPresence(self, self.DROP_DOWN_NAVIGATION_ROOT)

    def clickBlog(self):
        self.driver.find_element(By.XPATH, self.DROP_DOWN_NAVIGATION_ROOT + "//a[text()='Blog']").click()
        waitUtils.waitForElementPresence(self, self.BLOG_HEADER_ROOT)

    def clickDesignSchool(self):
        self.driver.find_element(By.XPATH, self.BLOG_NAVIGATION_LIST + "//a[text()='Design School']").click()
        waitUtils.waitTillUrlContains(self, "design-school")

    def clickTrends(self):
        self.driver.find_element(By.XPATH, self.BLOG_NAVIGATION_LIST + "//a[text()='Trends']").click()
        waitUtils.waitTillUrlContains(self, "trends")

    def clickPicsArtPro(self):
        self.driver.find_element(By.XPATH, self.BLOG_NAVIGATION_LIST + "//a[text()='Picsart Pro']").click()
        waitUtils.waitTillUrlContains(self, "picsart-pro")

    def clickNews(self):
        self.driver.find_element(By.XPATH, self.BLOG_NAVIGATION_LIST + "//a[text()='News']").click()
        waitUtils.waitTillUrlContains(self, "news")