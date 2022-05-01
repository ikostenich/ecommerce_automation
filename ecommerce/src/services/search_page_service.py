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
    
    def get_products_names(self, timeout=2):
        product_names = WebDriverWait(
            self.driver, timeout
            ).until(EC.visibility_of_any_elements_located(self.search_page.PRODUCT_NAME_LOCATOR))
        product_names = [i.text for i in product_names]
        return product_names
    
    def basic_search(self, text):
        self.search_page.search_keyword_input.element.clear()
        self.search_page.search_keyword_input.input_text(text)
        self.search_page.search_button.click()
        product_names = self.get_products_names()
        return product_names

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

    def get_products(self):
        products = []
        products_elements = self.search_page.product_boxes
        for product_element in products_elements:
            product = Product(product_element)
            products.append(product)
            print('test')
        return products