from selenium import webdriver
from pages_.loginWithProtectedFuncs import LoginPage
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

logInPageObject = LoginPage(driver)
# if logInPageObject._get_title() != "Amazon Sign-In":
#     print("Error: Wrong Page Title.")
#     exit(3)

logInPageObject.fill_username_field("syuzannademirtshyan@gmail.com")
logInPageObject.validate_continue_button_text()
logInPageObject.click_to_continue_button()
logInPageObject.fill_password_field("Adriana2023*")
sleep(5)
# Before confirming the password and clicking to the sign in button, I have scheduled a sleep time, so that the site does not force the CAPTCHA tool.
logInPageObject.click_to_sign_in_button()
sleep(5)
# I scheduled a sleep time to be sure that the code is working and the sign in was successfully done.

driver.close()
