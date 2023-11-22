from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from pages_.searchResultPage import SearchResultPage
from pages_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogin


class ProductDeletion(BaseTestWithLogin):

    def test_for_empty_cart(self):
        navigationBarObject = NavigationBar(self.driver)
        cartPageObject = CartPage(self.driver)
        if navigationBarObject.get_cart_count() != 0:
            navigationBarObject.click_to_cart_button()
            cartPageObject.delete_all_products_from_cart(cartProductsCount=navigationBarObject.get_cart_count())
        navigationBarObject.validate_empty_cart_with_products_count()

    def test_for_deletion_first_product_from_cart(self):
        navigationBarObject = NavigationBar(self.driver)
        cartPageObject = CartPage(self.driver)
        searchResultPageObject = SearchResultPage(self.driver)
        productDetailsPageObject = ProductDetailsPage(self.driver)
        cartProductsCount = navigationBarObject.get_cart_count()
        if cartProductsCount == 0:
            navigationBarObject.fill_search_field("Smart Case for Apple AirPods Max Supports Sleep Mode")
            navigationBarObject.click_to_search_button()
            searchResultPageObject.click_on_first_product_from_list()
            productDetailsPageObject.click_to_add_to_cart_button()
        navigationBarObject.click_to_cart_button()
        cartPageObject.delete_first_product_from_cart()
        cartProductsCountAfterDeletionFirstProduct = navigationBarObject.get_cart_count()
        if cartProductsCountAfterDeletionFirstProduct == 0:
            self.assertEqual(cartPageObject.validate_empty_cart_with_message(), "Your Amazon Cart is empty.")
        else:
            self.assertEqual(cartProductsCount - 1, cartProductsCountAfterDeletionFirstProduct)

    def test_for_deletion_all_product_from_cart(self):
        navigationBarObject = NavigationBar(self.driver)
        cartPageObject = CartPage(self.driver)
        navigationBarObject.click_to_cart_button()
        if navigationBarObject.get_cart_count() == 0:
            self.assertEqual("Your Amazon Cart is empty.", cartPageObject.validate_empty_cart_with_message())
        else:
            cartPageObject.delete_all_products_from_cart(cartProductsCount=navigationBarObject.get_cart_count())
            self.assertEqual("Your Amazon Cart is empty.", cartPageObject.validate_empty_cart_with_message())
