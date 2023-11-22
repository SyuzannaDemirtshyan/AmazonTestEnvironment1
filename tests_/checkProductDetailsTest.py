from tests_.baseTest import BaseTestWithLogin
from pages_.navigationBar import NavigationBar
from pages_.searchResultPage import SearchResultPage
from pages_.productDetailsPage import ProductDetailsPage


class CheckProductDetails(BaseTestWithLogin):
    def test_for_validation_product_name_and_price(self):
        navigationBarObject = NavigationBar(self.driver)
        navigationBarObject.fill_search_field("Fitbit Charge 6 Fitness Tracker with Google apps")
        navigationBarObject.click_to_search_button()
        searchResultPageObject = SearchResultPage(self.driver)
        name = searchResultPageObject.get_first_product_name()
        price = searchResultPageObject.get_first_product_price()
        searchResultPageObject.click_on_first_product_from_list()
        productDetailsPageObject = ProductDetailsPage(self.driver)
        expectedName = productDetailsPageObject.get_product_name()
        expectedPrice = productDetailsPageObject.get_product_price()

        self.assertEqual(name, expectedName, "ERROR: names do not match")
        self.assertEqual(price, expectedPrice, "ERROR: prices do not match")
