from selenium.webdriver.common.by import By

from ecommerce.src.pages.home_page import HomePage
from ecommerce.src.utilities.elements.base_element import BaseElement

class ProductPage(HomePage):
  
    def __init__(self, driver):
        self.driver = driver
    
    @property
    def page_title(self):
        PRODUCT_TITLE_LOCATOR = (By.XPATH, '//div[@class="product-name"]/h1')
        return BaseElement(self.driver, locator=PRODUCT_TITLE_LOCATOR)