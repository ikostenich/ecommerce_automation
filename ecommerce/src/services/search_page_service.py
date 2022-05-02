from re import sub
from decimal import Decimal
import random

from selenium.common.exceptions import TimeoutException

from ecommerce.src.objects.product import Product
from ecommerce.src.objects.pager import Pager
from ecommerce.src.pages.search_page import SearchPage
from ecommerce.src.pages.product_page import ProductPage


class SearchPageService:


    def __init__(self, driver):
        self.driver = driver
        self.search_page = SearchPage(self.driver)
        self._pager = None
    

    @property
    def page(self):
        return self.search_page
    

    @property
    def pager(self):
        return self._pager
    

    @staticmethod
    def get_product_names(products):

        if products:
            product_names = [i.product_title.text for i in products]
        else:
            return []

        return product_names
    

    @staticmethod
    def get_product_prices(products):

        def convert_to_decimal(product):
            if product.product_price:
                return Decimal(sub(r'[^\d.]', '', product.product_price.text.split(maxsplit=1)[0]))
            else:
                return Decimal(0)
            
        product_prices = [convert_to_decimal(i) for i in products]

        return product_prices
  
   
    def get_pager(self):
        pager = self.search_page.pager
        if pager:
            self._pager = Pager(pager)
        return pager


    def get_products(self, all=True):
        products = []
        self.search_page.products = []

        if all:
            try:
                self.page.select_display_number(self.search_page.display_dropdown.get_values()[-1])
            except TimeoutException:
                return

        products_elements = self.search_page.product_boxes
        for product_element in products_elements:
            product = Product(product_element)
            products.append(product)

        self.search_page.products = products

        return products
   

    def basic_search(self, text, expected_product_name=None):
        self.search_page.search_keyword_input.set_default()
        self.search_page.search_keyword_input.input_text(text)
        self.search_page.search_button.click()
        products = self.get_products()

        if expected_product_name:
            product_names = SearchPageService.get_product_names(products)
            assert expected_product_name in product_names, f'Product {expected_product_name} not found in search results.' \
                                                    f'Search results: {product_names}'

        return products


    def advanced_search(self, text, expected_product_name=None, **kwargs):

        category = None
        search_subcategories = None
        manufacturer = None
        search_in_description = None

        if 'category' in kwargs.keys():
            category = kwargs['category']
        if 'search_subcategories' in kwargs.keys():
            search_subcategories = kwargs['search_subcategories']
        if 'manufacturer' in kwargs.keys():
            manufacturer = kwargs['manufacturer']
        if 'search_in_description' in kwargs.keys():
            search_in_description = kwargs['search_in_description']

        if not self.page.is_advanced_search_selected():
            self.page.check_advanced_search()
        else:
            self.search_page.category_dropdown.set_default()
            self.search_page.manufacturer_dropdown.set_default()
            self.search_page.search_subcategories_checkbox.set_default()
            self.search_page.search_in_description_checkbox.set_default()
        
        if category:
            self.search_page.category_dropdown.select_value(category)
        if search_subcategories:
            self.search_page.search_subcategories_checkbox.click()
        if manufacturer:
            self.search_page.manufacturer_dropdown.select_value(manufacturer)
        if search_in_description:
            self.search_page.search_in_description_checkbox.click()            

        products = self.basic_search(text, expected_product_name)
                                                    
        return products
    

    def sort_name(self, reversed=False):

        sorting_options = {
            "name_straight_order": 'Name: A to Z',
            "name_reversed_order": 'Name: Z to A'
        }

        if not reversed:
            self.search_page.sort_by_dropdown.select_value(sorting_options['name_straight_order'])
        else:
            self.search_page.sort_by_dropdown.select_value(sorting_options['name_reversed_order'])

        self.search_page.wait_for_products_update()

        products = self.get_products()
        product_names = SearchPageService.get_product_names(products)

        return product_names


    def sort_price(self, reversed=False):

        sorting_options = {
            "price_straight_order": 'Price: Low to High',
            "price_reversed_order": 'Price: High to Low'
        }

        if not reversed:
            self.search_page.sort_by_dropdown.select_value(sorting_options['price_straight_order'])
        else:
            self.search_page.sort_by_dropdown.select_value(sorting_options['price_reversed_order'])

        self.search_page.wait_for_products_update()

        products_objects = self.get_products()
        products = zip(SearchPageService.get_product_names(products_objects), SearchPageService.get_product_prices(products_objects))

        return list(products)
        

    def add_random_product_to_cart(self):
        sucess_message = 'The product has been added to your shopping cart'

        products = self.search_page.products
        products_list = [product for product in products if product.add_to_cart_button.text == 'ADD TO CART']
        random_product = random.choice(products_list)
        random_product.add_to_cart_button.click()
        success_notification = self.search_page.bar_notification_success
        assert success_notification, f"Product {random_product.text} wasn't added to cart"
        assert success_notification.text == sucess_message, f'Message displayed is invalid. Expected: {sucess_message}' \
                                                            f'Actual: {success_notification.text} '
        self.search_page.bar_notification_close.click()


    def add_random_product_to_comparison(self):
        sucess_message = 'The product has been added to your product comparison'

        products = self.search_page.products
        products_list = [product for product in products]
        random_product = random.choice(products_list)
        random_product.add_to_compare_button.click()
        success_notification = self.search_page.bar_notification_success
        assert success_notification, f"Product {random_product.text} wasn't added to comparison"
        assert success_notification.text == sucess_message, f'Message displayed is invalid. Expected: {sucess_message}' \
                                                            f'Actual: {success_notification.text} '
        self.search_page.bar_notification_close.click()


    def add_random_product_to_wishlist(self):
        sucess_message = 'The product has been added to your wishlist'

        products = self.search_page.products
        products_list = [product for product in products]
        random_product = random.choice(products_list)
        random_product.add_to_wishlist_button.click()
        success_notification = self.search_page.bar_notification_success
        assert success_notification, f"Product {random_product.text} wasn't added to wishlist"
        assert success_notification.text == sucess_message, f'Message displayed is invalid. Expected: {sucess_message}' \
                                                            f'Actual: {success_notification.text} '
        self.search_page.bar_notification_close.click()


    def open_random_product(self):
        products = self.search_page.products
        products_list = [product for product in products]
        random_product = random.choice(products_list)
        random_product_name = random_product.product_title.text
        random_product.product_title_link.click()
        product_page = ProductPage(self.driver)
        assert random_product_name == product_page.page_title.text, f'Name of random product {random_product} doesnt match' \
                                                                    f'random page title: {product_page.page_title.text}'
        
        return product_page


    def select_display_value(self, value):
        
        self.search_page.display_dropdown.select_value(str(value))
        self.search_page.wait_for_products_update()

        products = self.get_products(all=False)

        return products