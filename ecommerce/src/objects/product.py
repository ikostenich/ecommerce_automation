from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ecommerce.src.utilities.elements.base_element import BaseElement


class Product:
    
    def __init__(self, product_box_element):
        self.product_box = product_box_element

    @property
    def product_title(self):
        PRODUCT_TITLE_LOCATOR = (By.XPATH, './/h2[@class="product-title"]')
        return BaseElement(self.product_box, locator=PRODUCT_TITLE_LOCATOR)
    
    @property
    def product_image(self):
        PRODUCT_IMAGE_LOCATOR = (By.XPATH, './/img')
        return BaseElement(self.product_box, locator=PRODUCT_IMAGE_LOCATOR)

    @property
    def product_price(self):
        PRODUCT_PRICE_LOCATOR = (By.XPATH, ".//span[contains(@class, 'actual-price')]")
        return BaseElement(self.product_box, locator=PRODUCT_PRICE_LOCATOR)

    @property
    def product_rating(self):
        PRODUCT_RATING_LOCATOR = (By.XPATH, ".//div[@class='rating']/div")
        return BaseElement(self.product_box, locator=PRODUCT_RATING_LOCATOR)
