from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ecommerce.src.utilities.base_element import BaseElement


class Product:
    
    def __init__(self, driver, product_box_element):
        self.driver = driver
    #     self._name = None
    #     self._image = None
    #     self._price = None
    #     self._rating = None

    # @property
    # def name(self):
    #     return self._name
    
    # @property
    # def image(self):
    #     return self._image

    # @property
    # def price(self):
    #     return self._price

    # @property
    # def rating(self):
    #     return self._rating

    # @property
    # def product_boxes(self, timeout=2):
    #     PRODUCT_BOX_LOCATOR = (By.XPATH, "//div[@class='item-box']")
    #     elements = WebDriverWait(
    #         self.driver, timeout
    #         ).until(EC.visibility_of_all_elements_located(PRODUCT_BOX_LOCATOR))
    #     return elements
    
    # getPrice(WebElement product_box){
    #     return product_box.findElement(By.Xpath, ".xpath");
    # }
    @property
    def product_title(self):
        PRODUCT_TITLE_LOCATOR = (By.XPATH, './/h2[@class="product-title"]')
        return BaseElement(self.driver, locator=PRODUCT_TITLE_LOCATOR)
