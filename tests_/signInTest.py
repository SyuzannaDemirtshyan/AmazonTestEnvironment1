import unittest
from selenium import webdriver
from time import sleep
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class SignIn(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positiveSignIn(self):
        signInPageObject = LoginPage(self.driver)
        signInPageObject.fill_username_field("syuzannademirtshyan@gmail.com")
        signInPageObject.click_to_continue_button()
        signInPageObject.fill_password_field("Adriana2023*")
        sleep(5)
        signInPageObject.click_to_signin_button()
        sleep(5)

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_negativeSignIn_invalidPassword(self):
        signInPageObject = LoginPage(self.driver)
        signInPageObject.fill_username_field("syuzannademirtshyan@gmail.com")
        signInPageObject.click_to_continue_button()
        signInPageObject.fill_password_field("wrongPassword")
        signInPageObject.click_to_signin_button()

        self.assertEqual("Your password is incorrect", signInPageObject.get_incorrect_password_error_message_text())

    def test_negativeSignIn_invalidEmail(self):
        signInPageObject = LoginPage(self.driver)
        signInPageObject.fill_username_field("wrongEmail")
        signInPageObject.click_to_continue_button()

        self.assertEqual("We cannot find an account with that email address",
                         signInPageObject.get_incorrect_email_error_message_text())

    def tearDown(self):
        self.driver.close()
