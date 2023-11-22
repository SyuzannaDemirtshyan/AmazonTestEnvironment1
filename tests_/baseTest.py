import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import mainPageUrl, signInPageUrl, validUser
from time import sleep
from pages_.loginPage import LoginPage


class BaseTestWithoutLogin(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()


class BaseTestWithLogin(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(signInPageUrl)
        self.signInPageObject = LoginPage(self.driver)
        self.signInPageObject.fill_username_field(validUser.userName)
        self.signInPageObject.click_to_continue_button()
        self.signInPageObject.fill_password_field(validUser.password)
        sleep(5)  # time sleep is done to avoid captcha given by Amazon website
        self.signInPageObject.click_to_signin_button()

    def tearDown(self):
        self.driver.close()
