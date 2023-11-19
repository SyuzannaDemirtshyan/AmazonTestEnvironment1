import unittest
from selenium import webdriver
from time import sleep
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage


class ProductDeletion(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.signInPageObject = LoginPage(self.driver)
        self.signInPageObject.fill_username_field("syuzannademirtshyan@gmail.com")
        self.signInPageObject.click_to_continue_button()
        self.signInPageObject.fill_password_field("Adriana2023*")
        sleep(5)  # time sleep is done to avoid captcha given by Amazon website
        self.signInPageObject.click_to_signin_button()

    def test_for_empty_cart(self):
        cartPageObject = NavigationBar(self.driver)
        cartPageObject.click_to_cart_button()
        cartPageObject = CartPage(self.driver)
        cartPageObject.validate_empty_cart()

    def test_for_deletion_first_product_from_cart(self):
        cartPageObject = NavigationBar(self.driver)
        cartPageObject.click_to_cart_button()
        cartPageObject = CartPage(self.driver)
        cartProductsCount = cartPageObject.get_cart_count()
        cartPageObject.delete_first_product_from_cart()
        cartProductsCountAfterDeletionFirstProduct = cartPageObject.get_cart_count()

        self.assertEqual(cartProductsCount - 1, cartProductsCountAfterDeletionFirstProduct)

    def test_for_deletion_all_product_from_cart(self):
        cartPageObject = NavigationBar(self.driver)
        cartPageObject.click_to_cart_button()
        cartPageObject = CartPage(self.driver)
        cartProductsCount = cartPageObject.get_cart_count()
        while cartProductsCount != 0:
            cartPageObject.delete_first_product_from_cart()
            cartProductsCount -= 1

    def tearDown(self):
        self.driver.close()
