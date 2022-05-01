from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ecommerce.src.utilities.elements.base_element import BaseElement
from ecommerce.src.utilities.elements.dropdown_element import DropdownElement
from ecommerce.src.utilities.elements.checkbox_element import CheckboxElement
from ecommerce.src.pages.home_page import HomePage


class SearchPage(HomePage):

    url = 'https://demo.nopcommerce.com/search'
  
    def __init__(self, driver):
        self.driver = driver 
        self._products = []
    
    @property
    def page_title(self):
        SEARCH_FIELD_LOCATOR = (By.XPATH, '//div[@class="page-title"]/h1')
        return BaseElement(self.driver, locator=SEARCH_FIELD_LOCATOR)

    @property
    def search_keyword_input(self):
        SEARCH_BUTTON_LOCATOR = (By.ID, 'q')
        return BaseElement(self.driver, locator=SEARCH_BUTTON_LOCATOR)    

    @property
    def advanced_search_checkbox(self):
        ADVANCED_SEARCH_CHECKBOX_LOCATOR = (By.ID, 'advs')
        return CheckboxElement(self.driver, locator=ADVANCED_SEARCH_CHECKBOX_LOCATOR, default_value=False)
    
    @property
    def category_dropdown(self):
        CATEGORY_DROPDOWN_LOCATOR = (By.ID, 'cid')
        return DropdownElement(self.driver, locator=CATEGORY_DROPDOWN_LOCATOR)
    
    @property
    def search_subcategories_checkbox(self):
        SEARCH_SUBCATEGORIES_CHECKBOX_LOCATOR = (By.ID, 'isc')
        return CheckboxElement(self.driver, locator=SEARCH_SUBCATEGORIES_CHECKBOX_LOCATOR, default_value=False)
    
    @property
    def manufacturer_dropdown(self):
        MANUFACTURER_DROPDOWN_LOCATOR = (By.ID, 'mid')
        return DropdownElement(self.driver, locator=MANUFACTURER_DROPDOWN_LOCATOR)
    
    @property
    def search_in_description_checkbox(self):
        SEARCH_IN_DESCRIPTION_CHECKBOX_LOCATOR = (By.ID, 'sid')
        return CheckboxElement(self.driver, locator=SEARCH_IN_DESCRIPTION_CHECKBOX_LOCATOR, default_value=False)
    
    @property
    def search_button(self):
        SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'search-button')]")
        return BaseElement(self.driver, locator=SEARCH_BUTTON_LOCATOR)

    @property
    def no_result_message(self):
        NO_RESULT_MESSAGE_LOCATOR = (By.CLASS_NAME, "no-result")
        return BaseElement(self.driver, locator=NO_RESULT_MESSAGE_LOCATOR)


    @property
    def product_boxes(self, timeout=2):
        PRODUCT_BOX_LOCATOR = (By.XPATH, "//div[@class='item-box']")
        try:
            products = WebDriverWait(
                self.driver, timeout
                ).until(EC.visibility_of_all_elements_located(PRODUCT_BOX_LOCATOR))
        except TimeoutException:
            products = []

        return products

    @property
    def products(self):
        return self._products
    
    @products.setter
    def products(self, value):
        self._products = value