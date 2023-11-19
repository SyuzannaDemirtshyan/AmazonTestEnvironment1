from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "//input[@value='Delete'][1]")
        self.__compareWithSimilarItemsButtonLocator = (By.XPATH, "//input[@value='Compare with similar items'][1]")
        self.__closeCompareWithSimilarItemsButtonLocator = (By.CLASS_NAME, "a-icon a-icon-close")
        self.__saveForLaterButtonLocator = (By.XPATH, "//input[@value='Save for later'][1]")
        self.__moveToCartButtonLocator = (By.ID, "a-autoid-6")
        self.__cartCountLocator = (By.ID, "nav-cart-count")

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

    def validate_empty_cart(self):
        cartCounElement = self._find_element(self.__cartCountLocator)
        if int(self._get_text(cartCounElement)) == 0:
            print("Warning! The Cart Is Empty")

    def get_cart_count(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        return int(self._get_text(cartCountElement))
