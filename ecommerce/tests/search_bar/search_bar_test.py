import pytest

from ecommerce.src.pages.base_page import BasePage


pytestmark = [pytest.mark.smoke]


@pytest.mark.usefixtures('init_driver')
class TestSearchBar:
    
    @pytest.mark.tcid10
    def test_search_full_product_name(self):
        
        product_name = 'Apple iCam'

        base_website = BasePage(self.driver)
        search_bar = base_website.search_bar

        base_website.open_website()

        search_bar.enter_search_text(product_name)

        search_bar.click_search_button()


