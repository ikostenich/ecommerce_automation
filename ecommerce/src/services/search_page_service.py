from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ecommerce.src.objects.product import Product

from ecommerce.src.pages.search_page import SearchPage


class SearchPageService:

    def __init__(self, driver):
        self.driver = driver
        self.search_page = SearchPage(self.driver)
    
    @property
    def page(self):
        return self.search_page

    def open_search_page(self):
        self.search_page.open_page()
    
    def get_search_page_title(self):
        return self.search_page.page_title.text
    
    def is_advanced_search_selected(self):
        advanced_search_checkbox = self.search_page.advanced_search_checkbox
        is_selected = advanced_search_checkbox.element.is_selected()
        return is_selected

    def is_category_dropdown_visible(self):
        return self.search_page.category_dropdown.is_displayed
    
    def is_search_subcategories_checkbox_visible(self):
        return self.search_page.search_subcategories_checkbox.is_displayed

    def is_manufacturer_dropdown_visible(self):
        return self.search_page.manufacturer_dropdown.is_displayed
    
    def is_search_in_description_dropdown_visible(self):
        return self.search_page.search_in_description_checkbox.is_displayed
    
    def check_advanced_search(self):
        self.search_page.advanced_search_checkbox.click()

    def get_products(self):
        products = []
        products_elements = self.search_page.product_boxes
        for product_element in products_elements:
            product = Product(product_element)
            products.append(product)
        
        self.search_page.products = products
        return products
    
    @staticmethod
    def get_product_names(products):
        product_names = [i.product_title.text for i in products]
        return product_names
    

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

        if not self.is_advanced_search_selected():
            self.check_advanced_search()
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