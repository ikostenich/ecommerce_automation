from ecommerce.src.helpers.config_helpers import get_base_url
from ecommerce.src.pages.base_page import BasePage


class HomePage(BasePage):

    url = get_base_url()

    def open_home_page(self):
        self.driver.get(self.url)
