from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super(SearchResultPage, self).__init__(driver)
        self.__firstProductLocator = (By.XPATH, "//div[@class='a-section aok-relative s-image-fixed-height'][1]")
        self.__firstProductNameLocator = (By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[1]")
        self.__firstProductPriceLocator = (By.XPATH, "(//span[@class='a-price'])[1]")

    def click_on_first_product_from_list(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click_to_element(firstProductElement)

    def get_first_product_name(self):
        firstProductNameElement = self._find_element(self.__firstProductNameLocator)
        return self._get_text(firstProductNameElement)

    def get_first_product_price(self):
        firstProductPriceElement = self._find_element(self.__firstProductPriceLocator)
        return self._get_text(firstProductPriceElement)
