import pytest

from ecommerce.src.pages.home_page import BasePage, HomePage
from ecommerce.src.pages.search_bar import SearchBar
import time


pytestmark = [pytest.mark.smoke]


# @pytest.mark.usefixtures('init_driver')
# class TestSearchBar:
    
#     @pytest.mark.tc10
#     def test_search_full_product_name(self):
        
#         product_name = 'Apple iCam'

#         home_page = HomePage(self.driver)
#         home_page.open_page()

#         search_bar = SearchBar(self.driver)
#         search_bar.search_input.input_text(product_name)

#         search_bar.click_search_button()

        

