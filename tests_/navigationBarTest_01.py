from selenium import webdriver
from time import sleep
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(
    "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObject = LoginPage(driver)
loginPageObject.fill_username_field("syuzannademirtshyan@gmail.com")
loginPageObject.click_to_continue_button()
loginPageObject.fill_password_field("Adriana2023*")
sleep(5)
# Before confirming the password and clicking to the sign in button, I have scheduled a sleep time, so that the site does not force the CAPTCHA tool
loginPageObject.click_to_signin_button()
sleep(5)
# I scheduled a sleep time to be sure that the code is working and the sign in was successfully done.


navigationBarObject = NavigationBar(driver)
navigationBarObject.fill_search_field_element("Smart Case for Apple AirPods Max Supports Sleep Mode")
navigationBarObject.click_to_search_button()
navigationBarObject.click_to_the_searched_first_product()
navigationBarObject.click_to_add_to_cart_button()

driver.close()
