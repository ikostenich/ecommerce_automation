import pytest
from ecommerce.src.pages.search_page import SearchPage
from ecommerce.src.services.search_page_service import SearchPageService    


@pytest.mark.usefixtures('driver')
class TestSearchPage:

    @pytest.fixture(scope='class')
    def search_page_service(self):

        search_page_service = SearchPageService(self.driver)

        yield search_page_service


    # @pytest.mark.tc14
    # def test_verify_search_page_title(self, search_page_service):
     
    #     search_page_service.open_search_page()    
        
    #     page_title = 'Search'
    #     assert search_page_service.get_search_page_title() == page_title, f'{page_title} page title is invalid. Expected: {page_title}. Actual: {search_page_service.get_search_page_title()}'

    
    product_name_search_data = ['Apple iCam', 'Apple', 'App']

    # @pytest.mark.tc25
    # @pytest.mark.tc26
    # @pytest.mark.tc27
    # @pytest.mark.parametrize('search_data', product_name_search_data)
    # def test_search_by_full_name(self, search_page_service, search_data):

    #     product_title = 'Apple iCam'

    #     search_page_service.open_search_page()

    #     product_names = search_page_service.basic_search(search_data)

    #     assert product_title in product_names, f'Product {product_title} not found in search results.' \
    #                                             f'Search results: {product_names}'


    # @pytest.mark.tc32
    # @pytest.mark.tc33
    # @pytest.mark.tc34
    # @pytest.mark.tc35
    # @pytest.mark.tc36
    # def test_advanced_search_checkbox(self, search_page_service):

    #     search_page_service.open_search_page()
    #     assert not search_page_service.is_advanced_search_selected(), 'Advanced search checkbox is enabled by default'

    #     search_page_service.page.advanced_search_checkbox.click()
    #     assert search_page_service.is_category_dropdown_visible(), 'Category dropdown is not visible with "advances search" checkbox enabled'
    #     assert search_page_service.is_search_subcategories_checkbox_visible(), 'Search subcategories checkbox is not visible with "advances search" checkbox enabled'
    #     assert search_page_service.is_manufacturer_dropdown_visible(), 'Manufacturer dropdown is not visible with "advances search" checkbox enabled'
    #     assert search_page_service.is_search_in_description_dropdown_visible(), 'Search in product description checkbox is not visible with "advances search" checkbox enabled'
       
    @pytest.mark.tc49
    @pytest.mark.parametrize('search_data', product_name_search_data)
    def test_search_by_product_name(self, search_page_service, search_data):

        product_title = 'Apple iCam'

        search_page_service.open_search_page()
        search_page_service.page.advanced_search_checkbox.click()

        product_names = search_page_service.basic_search(search_data)

        assert product_title in product_names, f'Product {product_title} not found in search results.' \
                                                f'Search results: {product_names}'
        
        products = search_page_service.get_products()


    # @pytest.mark.tc49
    # @pytest.mark.parametrize('search_data', product_name_search_data)
    # def test_search_by_full_name(self, search_page_service, search_data):

    #     product_title = 'Apple iCam'

    #     search_page_service.open_search_page()
    #     search_page_service.page.advanced_search_checkbox.click()

    #     product_names = search_page_service.basic_search(search_data)

    #     assert product_title in product_names, f'Product {product_title} not found in search results.' \
    #                                             f'Search results: {product_names}'