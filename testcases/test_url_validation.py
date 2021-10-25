import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from picsartPageObjects.blogsearchpage import blogSearchPage
from picsartPageObjects.loginpage import loginPage
from picsartPageObjects.homepage import homePage
from picsartPageObjects.logoutpage import loginOutPage
from picsartPageObjects.navigationheader import navigationHeaderPage

class Test_Login:

    def test_logout_url(self):
        serv = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://picsart.com/")
        homePage(driver).clickLoginButton()
        loginPg = loginPage(driver)
        loginPg.enterUserName('dg18021990@gmail.com')
        loginPg.enterPassword('India@123')
        loginPg.clickLogin().click()
        logOut = loginOutPage(driver)
        logOut.logoutUser()
        homePage(driver).clickLogo()
        url = driver.current_url
        if url == "https://picsart.com/":
            assert True
        else:
            print(url + " is not equals to https://picsart.com/")
            assert False
        driver.quit()

    def test_login_url(self):
        serv = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://picsart.com/")
        homePage(driver).clickLoginButton()
        loginPg = loginPage(driver)
        loginPg.enterUserName('dg18021990@gmail.com')
        loginPg.enterPassword('India@123')
        loginPg.clickLogin()
        url = driver.current_url
        if url == "https://picsart.com/create":
            assert True
        else:
            assert False
        driver.quit()

    def test_category_buttons(self):
        serv = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://picsart.com/")
        navigationHeaderPg = navigationHeaderPage(driver)
        navigationHeaderPg.clickLearn()
        navigationHeaderPg.clickBlog()
        url = driver.current_url
        if url == "https://picsart.com/blog":
            assert True
        else:
            print(url + " is not equals to https://picsart.com/blog")
            assert False
        navigationHeaderPg.clickDesignSchool()
        url = driver.current_url
        if url == "https://picsart.com/blog/category/design-school":
            assert True
        else:
            print(url + " is not equals to https://picsart.com/blog/category/design-school")
            assert False
        navigationHeaderPg.clickTrends()
        url = driver.current_url
        if url == "https://picsart.com/blog/category/trends":
            assert True
        else:
            print(url + " is not equals to https://picsart.com/blog/category/trends")
            assert False
        navigationHeaderPg.clickPicsArtPro()
        url = driver.current_url
        if url == "https://picsart.com/blog/category/picsart-pro":
            assert True
        else:
            print(url + " is not equals to https://picsart.com/blog/category/picsart-pro")
            assert False
        navigationHeaderPg.clickNews()
        url = driver.current_url
        if url == "https://picsart.com/blog/category/news":
            assert True
        else:
            print(url + " is not equals to https://picsart.com/blog/category/news")
            assert False
        driver.quit()

    def test_blog_search(self):
        serv = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://picsart.com/")
        navigationHeaderPg = navigationHeaderPage(driver)
        navigationHeaderPg.clickLearn()
        navigationHeaderPg.clickBlog()
        blogSearchPg = blogSearchPage(driver)
        search_out = blogSearchPg.search("animals")
        if search_out == "animals":
            assert True
        else:
            print(search_out + " is not equals to animals")
            assert False