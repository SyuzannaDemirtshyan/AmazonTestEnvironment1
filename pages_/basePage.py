from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator)))
            print(f"Element with locator: {locator[1]} found")
            return element
        except:
            print("Error: Element Not found")
            exit(1)

    def _click_to_element(self, webElement):
        webElement.click()

    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)

    def _get_title(self):
        return self.driver.title

    def _get_text(self, webElement):
        return webElement.text
