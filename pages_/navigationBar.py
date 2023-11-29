from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import logger


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartButtonLocator = (By.ID, "nav-cart-text-container")
        self.__cartCountLocator = (By.ID, "nav-cart-count")
        self.__accountAndListsContainerLocator = (By.ID, "nav-link-accountList")
        self.__signOutButtonLocator = (By.ID, "nav-item-signout")

    def fill_search_field(self, text):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click_to_element(searchButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_element(cartButtonElement)

    def validate_empty_cart_with_products_count(self):
        cartCounElement = self._find_element(self.__cartCountLocator)
        if int(self._get_text(cartCounElement)) == 0:
            logger("INFO", "Your cart is empty.")
        else:
            logger("ERROR", "Your cart is not empty.")
            exit(5)

    def get_cart_count(self):
        cartCountElement = self._find_element(self.__cartCountLocator)
        return int(self._get_text(cartCountElement))

    def move_mouse_to_account_and_lists_container(self):
        accountAndListsContainerElement = self._find_element(self.__accountAndListsContainerLocator)
        self._mouse_move(accountAndListsContainerElement)

    def click_on_sign_out_button(self):
        signOutButtonElement = self._find_element(self.__signOutButtonLocator)
        self._click_to_element(signOutButtonElement)
