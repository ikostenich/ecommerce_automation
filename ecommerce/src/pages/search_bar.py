from ecommerce.src.selenium_utils import SeleniumUtils

from ecommerce.src.pages.locators.search_bar_locators import SearchBarLocators


class SearchBar(SearchBarLocators):

    def __init__(self, driver):
        self.driver = driver
        self.se = SeleniumUtils(self.driver)
    
    def click_search_button(self):
        self.se.wait_and_click_element(self.SEARCH_BUTTON)
    
    def enter_search_text(self, text):
        self.se.wait_and_input_text(self.SEARCH_FIELD, text)

