from pkgutil import extend_path
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from ecommerce.src.utilities.elements.base_element import BaseElement


class Product:
    
    def __init__(self, product_box_element):
        self.product_box = product_box_element
    
    @property
    def product_title(self):
        PRODUCT_TITLE_LOCATOR = (By.XPATH, './/h2[@class="product-title"]')
        return BaseElement(self.product_box, locator=PRODUCT_TITLE_LOCATOR)

    @property
    def product_title_link(self):
        PRODUCT_TITLE_LINK_LOCATOR = (By.XPATH, './/h2[@class="product-title"]/a')
        return BaseElement(self.product_box, locator=PRODUCT_TITLE_LINK_LOCATOR)

    @property
    def product_image(self):
        PRODUCT_IMAGE_LOCATOR = (By.XPATH, './/img')
        return BaseElement(self.product_box, locator=PRODUCT_IMAGE_LOCATOR)

    @property
    def product_price(self):
        try:
            PRODUCT_PRICE_LOCATOR = (By.XPATH, ".//span[contains(@class, 'actual-price')]")
            return BaseElement(self.product_box, locator=PRODUCT_PRICE_LOCATOR)
        except TimeoutException:
            return None

    @property
    def product_rating(self):
        PRODUCT_RATING_LOCATOR = (By.XPATH, ".//div[@class='rating']/div")
        return BaseElement(self.product_box, locator=PRODUCT_RATING_LOCATOR)
    
    @property
    def add_to_cart_button(self):
        ADD_TO_CART_LOCATOR = (By.XPATH, ".//button[contains(@class, 'product-box-add-to-cart-button')]")
        return BaseElement(self.product_box, locator=ADD_TO_CART_LOCATOR)
    
    @property
    def add_to_compare_button(self):
        ADD_TO_COMPARE_LOCATOR = (By.XPATH, ".//button[contains(@class, 'add-to-compare-list-button')]")
        return BaseElement(self.product_box, locator=ADD_TO_COMPARE_LOCATOR)
    
    @property
    def add_to_wishlist_button(self):
        ADD_TO_WISHLIST_LOCATOR = (By.XPATH, ".//button[contains(@class, 'add-to-wishlist-button')]")
        return BaseElement(self.product_box, locator=ADD_TO_WISHLIST_LOCATOR)

