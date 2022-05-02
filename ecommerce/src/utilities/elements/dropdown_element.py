from ecommerce.src.utilities.elements.base_element import BaseElement

from selenium.webdriver.support.ui import Select


class DropdownElement(BaseElement):


    def __init__(self, driver, locator, default_timeout=2):
        super().__init__(driver, locator, default_timeout)
        self._select_element = Select(self._web_element)
        self.default_value = 'All'
    

    @property
    def is_displayed(self):
        return super().is_displayed


    def get_values(self):
        options = [i.text for i in self._select_element.options]
        return options
    

    def select_value(self, value):
        self._select_element.select_by_visible_text(value)
    
    
    def set_default(self):        
        self._select_element.select_by_visible_text(self.default_value)
    
