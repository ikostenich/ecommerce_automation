from ecommerce.src.utilities.elements.base_element import BaseElement


class CheckboxElement(BaseElement):


    def __init__(self, driver, locator, default_value, default_timeout=2):
        super().__init__(driver, locator, default_timeout)
        self.default_value = default_value
    

    @property
    def is_selected(self):
        return self.is_selected()
    

    def set_default(self):
        if not self.is_selected == self.default_value:
            self.click()
