import pytest

from ecommerce.src.services.search_bar_service import SearchBarService  


@pytest.mark.usefixtures('driver')
class TestSearchBar:


    @pytest.fixture(scope='class')
    def search_bar_service(self):

        search_bar_service = SearchBarService(self.driver)

        yield search_bar_service


    product_name_search_data = ['Apple iCam', 'Apple', 'App']

    @pytest.mark.tc10
    @pytest.mark.tc11
    @pytest.mark.tc12
    @pytest.mark.parametrize('search_data', product_name_search_data)
    def test_search_via_search_bar(self, search_bar_service, search_data):

        product_title = 'Apple iCam'

        search_bar_service.search(search_data, expected_product_name=product_title)
