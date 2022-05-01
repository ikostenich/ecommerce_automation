from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from ecommerce.src.utilities.elements.base_element import BaseElement


class Pager:
    def __init__(self, pager_element):
        self.pager_element = pager_element

    @property
    def next_page(self):
        NEXT_PAGE_LOCATOR = (By.XPATH, './/li[@class="next-page"]')
        return BaseElement(self.pager_element, locator=NEXT_PAGE_LOCATOR)
    
    def go_to_next_page(self):
        
        try:
            self.next_page.click()
        except TimeoutException:
            return False
        
        return True
    