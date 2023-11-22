from time import sleep
from pages_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidUserName, userWithInvalidPassword, signInPageUrl
from tests_.baseTest import BaseTestWithoutLogin


class SignIn(BaseTestWithoutLogin):

    def test_positiveSignIn(self):
        self.driver.get(signInPageUrl)
        signInPageObject = LoginPage(self.driver)
        signInPageObject.fill_username_field(validUser.userName)
        signInPageObject.click_to_continue_button()
        signInPageObject.fill_password_field(validUser.password)
        sleep(5)
        signInPageObject.click_to_signin_button()
        sleep(5)

        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def test_negativeSignIn_invalidPassword(self):
        signInPageObject = LoginPage(self.driver)
        signInPageObject.fill_username_field(userWithInvalidPassword.userName)
        signInPageObject.click_to_continue_button()
        signInPageObject.fill_password_field(userWithInvalidPassword.password)
        signInPageObject.click_to_signin_button()

        self.assertEqual("Your password is incorrect", signInPageObject.get_incorrect_password_error_message_text())

    def test_negativeSignIn_invalidEmail(self):
        signInPageObject = LoginPage(self.driver)
        signInPageObject.fill_username_field(userWithInvalidUserName.userName)
        signInPageObject.click_to_continue_button()

        self.assertEqual("We cannot find an account with that email address",
                         signInPageObject.get_incorrect_email_error_message_text())
