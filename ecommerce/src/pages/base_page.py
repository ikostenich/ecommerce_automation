from selenium.webdriver.common.by import By

from ecommerce.src.utilities.elements.base_element import BaseElement


class BasePage:

    url = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)
    
    @property
    def iframe(self):
        IFRAME_LOCATOR = (By.XPATH, "//iframe[@src]")

        return BaseElement(
            self.driver,
            locator=IFRAME_LOCATOR
            )
