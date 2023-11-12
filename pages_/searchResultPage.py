from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super(SearchResultPage, self).__init__(driver)
        self.__firstProductLocator = (By.XPATH, "//div[@class='a-section aok-relative s-image-fixed-height'][1]")

    def click_to_first_product(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click_to_element(firstProductElement)
