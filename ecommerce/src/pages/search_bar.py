from ecommerce.src.pages.home_page import HomePage
from selenium.webdriver.common.by import By

from ecommerce.src.utilities.base_element import BaseElement
from ecommerce.src.selenium_utils import SeleniumUtils


class SearchBar(HomePage):
  
    def __init__(self, driver):
        self.driver = driver
        self.se = SeleniumUtils(self.driver)
        self.__switch_to_iframe()

    def __switch_to_iframe(self):
        self.driver.switch_to.frame(self.iframe.element)        
    
    @property
    def search_input(self):
        SEARCH_FIELD_LOCATOR = (By.ID, 'small-searchterms')

        return BaseElement(
            self.driver,
            locator=SEARCH_FIELD_LOCATOR
            )

    @property
    def search_button(self):
        SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class,'search-box-button')]")

        return BaseElement(
            self.driver,
            locator=SEARCH_BUTTON_LOCATOR
            )

    def type_into_search_field(self, text):
        self.search_input.input_text(text)

    def click_search_button(self):
        self.search_button.click()
