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
    def products(self):
        return self._products
    

    @products.setter
    def products(self, value):
        self._products = value
    
    
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
    def sort_by_dropdown(self):
        SORT_BY_DROPDOWN = (By.ID, "products-orderby")
        return DropdownElement(self.driver, locator=SORT_BY_DROPDOWN)

    @property
    def display_dropdown(self):
        DISPLAY_DROPDOWN = (By.ID, "products-pagesize")
        return DropdownElement(self.driver, locator=DISPLAY_DROPDOWN)

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
    def pager(self, timeout=2):
        PAGER_LOCATOR = (By.XPATH, "//div[@class='pager']")
        try:
            pager_element = WebDriverWait(
                self.driver, timeout
                ).until(EC.visibility_of_element_located(PAGER_LOCATOR))
        except TimeoutException:
            pager_element = None

        return pager_element
    

    @property
    def bar_notification_success(self, timeout=2):
        BAR_NOTIFICATION_SUCCESS_LOCATOR = (By.XPATH, "//div[contains(@class, 'bar-notification success')]")

        try:
            success_notification = WebDriverWait(
                self.driver, timeout
                ).until(EC.visibility_of_element_located(BAR_NOTIFICATION_SUCCESS_LOCATOR))
        except TimeoutException:
            success_notification = None

        return success_notification
    

    @property
    def bar_notification_close(self):
        BAR_NOTIFICATION_CLOSE_LOCATOR = (By.XPATH, "//div[contains(@class, 'bar-notification success')]//span[@class='close']")
        return BaseElement(self.driver, locator=BAR_NOTIFICATION_CLOSE_LOCATOR)

    def wait_for_products_update(self):
        LOADING_SPINNER_LOCATOR = (By.XPATH, '//div[@class="ajax-products-busy"]')

        WebDriverWait(
            self.driver, 2
            ).until(EC.invisibility_of_element_located(LOADING_SPINNER_LOCATOR))
    

    def open_search_page(self):
        self.open_page()


    def get_page_title(self):
        return self.page_title.text
    

    def get_search_page_title(self):
        return self.page_title.text
    

    def is_advanced_search_selected(self):
        advanced_search_checkbox = self.advanced_search_checkbox
        is_selected = advanced_search_checkbox.element.is_selected()
        return is_selected


    def is_category_dropdown_visible(self):
        return self.category_dropdown.is_displayed
    

    def is_search_subcategories_checkbox_visible(self):
        return self.search_subcategories_checkbox.is_displayed


    def is_manufacturer_dropdown_visible(self):
        return self.manufacturer_dropdown.is_displayed
    

    def is_search_in_description_dropdown_visible(self):
        return self.search_in_description_checkbox.is_displayed
    

    def check_advanced_search(self):
        self.advanced_search_checkbox.click()
    

    def select_display_number(self, number):
        if number in self.display_dropdown.get_values():
            self.display_dropdown.select_value(number)
            self.wait_for_products_update()

    def is_pager_visible(self):
        return self.pager.is_displayed()
