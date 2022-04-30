from selenium.webdriver.common.by import By

from ecommerce.src.utilities.base_element import BaseElement


class BasePage:

    url = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)
    
    @property
    def iframe(self):
        IFRAME_LOCATOR = (By.XPATH, "//iframe[@src]")
        iframe = BaseElement(
            self.driver,
            locator=IFRAME_LOCATOR
            )