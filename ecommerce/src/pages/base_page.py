from ecommerce.src.helpers.config_helpers import get_base_url
from ecommerce.src.selenium_utils import SeleniumUtils
from ecommerce.src.pages.search_bar import SearchBar


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.se = SeleniumUtils(self.driver)
        self.search_bar = SearchBar(self.driver)
    
    def open_website(self):
        home_url = get_base_url()
        self.driver.get(home_url)