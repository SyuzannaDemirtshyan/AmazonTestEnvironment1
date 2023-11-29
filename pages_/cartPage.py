from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from pages_.navigationBar import NavigationBar


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "//input[@value='Delete'][1]")
        self.__compareWithSimilarItemsButtonLocator = (By.XPATH, "//input[@value='Compare with similar items'][1]")
        self.__closeCompareWithSimilarItemsButtonLocator = (By.CLASS_NAME, "a-icon a-icon-close")
        self.__saveForLaterButtonLocator = (By.XPATH, "//input[@value='Save for later'][1]")
        self.__moveToCartButtonLocator = (By.ID, "a-autoid-6")
        self.__cartIsEmptyMessageLocator = (By.CLASS_NAME, "a-spacing-mini.a-spacing-top-base")

    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click_to_element(firstProductDeleteButtonElement)

    def click_to_compare_with_similar_items_button(self):
        compareWithSimilarItemsButtonElement = self._find_element(self.__compareWithSimilarItemsButtonLocator)
        self._click_to_element(compareWithSimilarItemsButtonElement)

    def close_compare_with_similar_items_page(self):
        closeCompareWithSimilarItemsButtonElement = self._find_element(self.__closeCompareWithSimilarItemsButtonLocator)
        self._click_to_element(closeCompareWithSimilarItemsButtonElement)

    def click_to_save_for_later_button(self):
        saveForLaterButtonElement = self._find_element(self.__saveForLaterButtonLocator)
        self._click_to_element(saveForLaterButtonElement)

    def return_to_cart_saved_for_later_item(self):
        moveToCartButtonElement = self._find_element(self.__moveToCartButtonLocator)
        self._click_to_element(moveToCartButtonElement)

    def delete_all_products_from_cart(self):
        navigationBarObject = NavigationBar(self.driver)
        cartProductsCount = navigationBarObject.get_cart_count()
        while cartProductsCount != 0:
            self.delete_first_product_from_cart()
            cartProductsCount -= 1

    def get_text_message_of_empty_cart(self):
        cartIsEmptyMessageElement = self._find_element(self.__cartIsEmptyMessageLocator)
        return self._get_text(cartIsEmptyMessageElement)
