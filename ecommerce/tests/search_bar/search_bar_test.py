import pytest

from ecommerce.src.pages.home_page import BasePage, HomePage
from ecommerce.src.pages.search_bar import SearchBar
import time


pytestmark = [pytest.mark.smoke]


@pytest.mark.usefixtures('init_driver')
class TestSearchBar:
    
    @pytest.mark.tcid10
    def test_search_full_product_name(self):
        
        product_name = 'Apple iCam'
        welcome_text = 'Welcome to our store'

        home_page = HomePage(self.driver)
        # search_bar = base_website.search_bar

        home_page.open_page()

        search_bar = SearchBar(self.driver)
        search_bar.search_input.input_text(product_name)

        search_bar.click_search_button()

        

