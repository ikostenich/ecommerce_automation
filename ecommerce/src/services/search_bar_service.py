from ecommerce.src.pages.search_bar import SearchBar

from ecommerce.src.services.search_page_service import SearchPageService


class SearchBarService:


    def __init__(self, driver):
        self.driver = driver
        self.search_bar = SearchBar(self.driver)
    

    def search(self, text, expected_product_name=None):

        self.search_bar.search_input.set_default()
        self.search_bar.search_input.input_text(text)
        self.search_bar.search_button.click()
        search_page_service = SearchPageService(self.driver)
        products = search_page_service.get_products()

        if expected_product_name:
            product_names = SearchPageService.get_product_names(products)
            assert expected_product_name in product_names, f'Product {expected_product_name} not found in search results.' \
                                                    f'Search results: {product_names}'

        return products
    