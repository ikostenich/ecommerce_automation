import pytest
from ecommerce.src.pages.search_page import SearchPage
from ecommerce.src.services.search_page_service import SearchPageService    


@pytest.mark.usefixtures('driver')
class TestSearchPage:

    @pytest.fixture(scope='class')
    def search_page_service(self):

        search_page_service = SearchPageService(self.driver)

        yield search_page_service


    @pytest.mark.tc14
    def test_verify_search_page_title(self, search_page_service):
     
        search_page_service.open_search_page()    
        
        page_title = 'Search'
        assert search_page_service.get_search_page_title() == page_title, f'{page_title} page title is invalid. Expected: {page_title}. Actual: {search_page_service.get_search_page_title()}'

    
    product_name_search_data = ['Apple iCam', 'Apple', 'App']

    @pytest.mark.tc25
    @pytest.mark.tc26
    @pytest.mark.tc27
    @pytest.mark.parametrize('search_data', product_name_search_data)
    def test_search_by_full_name(self, search_page_service, search_data):

        product_title = 'Apple iCam'

        search_page_service.open_search_page()

        search_page_service.basic_search(search_data, expected_product_name=product_title)



    @pytest.mark.tc32
    @pytest.mark.tc33
    @pytest.mark.tc34
    @pytest.mark.tc35
    @pytest.mark.tc36
    def test_advanced_search_checkbox(self, search_page_service):

        search_page_service.open_search_page()
        assert not search_page_service.is_advanced_search_selected(), 'Advanced search checkbox is enabled by default'

        search_page_service.check_advanced_search()
        assert search_page_service.is_category_dropdown_visible(), 'Category dropdown is not visible with "advances search" checkbox enabled'
        assert search_page_service.is_search_subcategories_checkbox_visible(), 'Search subcategories checkbox is not visible with "advances search" checkbox enabled'
        assert search_page_service.is_manufacturer_dropdown_visible(), 'Manufacturer dropdown is not visible with "advances search" checkbox enabled'
        assert search_page_service.is_search_in_description_dropdown_visible(), 'Search in product description checkbox is not visible with "advances search" checkbox enabled'


    @pytest.mark.tc48
    def test_verify_categories_sorting(self, search_page_service):
     
        search_page_service.open_search_page()
        search_page_service.check_advanced_search()      
        values = search_page_service.page.category_dropdown.get_values()
        sorted_values = sorted(values)

        assert values == sorted_values, f'Categories are not sorted in ascehding ofder by name'

    @pytest.mark.tc49
    @pytest.mark.parametrize('search_data', product_name_search_data)
    def test_advanced_search_by_product_name(self, search_page_service, search_data):

        product_title = 'Apple iCam'

        search_page_service.open_search_page()
        search_page_service.advanced_search(search_data, expected_product_name=product_title)    


    @pytest.mark.tc52
    def test_verify_search_by_subcategory(self, search_page_service):
        
        search_keyword = 'Apple'
        product_title = 'Apple MacBook Pro 13-inch'

        search_params = {
            'category': 'Computers >> Notebooks',
        }

        search_page_service.open_search_page()
        search_page_service.advanced_search(search_keyword, expected_product_name=product_title, **search_params) 


    @pytest.mark.tc52
    def test_verify_search_by_subcategory_other_subcategories_not_displayed(self, search_page_service):
        
        search_keyword = 'Apple'
        not_displayed_title = 'Apple iCam'

        search_params = {
            'category': 'Computers >> Notebooks',
        }

        search_page_service.open_search_page()
        products = search_page_service.advanced_search(search_keyword, **search_params)
        product_names = SearchPageService.get_product_names(products)
        
        assert not not_displayed_title in product_names, f'{not_displayed_title} is at the results list.' \
                                                        f'Only items of {search_params["category"]} should be returned'

    @pytest.mark.tc58
    def test_verify_search_in_subcategories(self, search_page_service):
        
        search_keyword = 'Apple'
        product_title = 'Apple MacBook Pro 13-inch'

        search_params = {
            'category': 'Computers',
            'search_subcategories': True
        }

        search_page_service.open_search_page()
        search_page_service.advanced_search(search_keyword, expected_product_name=product_title, **search_params) 


    @pytest.mark.tc59
    def test_verify_search_not_displayed_other_subcategories(self, search_page_service):
        
        search_keyword = 'pro'
        not_displayed_title = 'Obey Propaganda Hat'

        search_params = {
            'category': 'Computers',
            'search_subcategories': True
        }

        search_page_service.open_search_page()
        products = search_page_service.advanced_search(search_keyword, **search_params)
        product_names = SearchPageService.get_product_names(products)
        
        assert not not_displayed_title in product_names, f'{not_displayed_title} is at the results list.' \
                                                         f'Only items of {search_params["category"]} should be returned'

    @pytest.mark.tc65
    def test_verify_search_by_manufacturer(self, search_page_service):
        
        search_keyword = 'Apple'
        product_title = 'Apple MacBook Pro 13-inch'

        search_params = {
            'manufacturer': 'Apple',
        }

        search_page_service.open_search_page()
        search_page_service.advanced_search(search_keyword, expected_product_name=product_title, **search_params) 

    @pytest.mark.tc66
    def test_verify_search_not_displayed_other_manufacturers(self, search_page_service):
        
        search_keyword = 'pro'
        not_displayed_title = 'Obey Propaganda Hat'

        search_params = {
            'manufacturer': 'Apple',
        }

        search_page_service.open_search_page()
        products = search_page_service.advanced_search(search_keyword, **search_params)
        product_names = SearchPageService.get_product_names(products)
        
        assert not not_displayed_title in product_names, f'{not_displayed_title} is at the results list.' \
                                                         f'Only items of {search_params["category"]} should be returned'

    @pytest.mark.tc71
    def test_verify_search_by_partial_description_not_checked(self, search_page_service):
        
        search_phrase = 'A groundbreaking Retina display'
        product_title = 'Apple MacBook Pro 13-inch'

        search_params = {
            'search_in_description': False,
        }

        search_page_service.open_search_page()
        products = search_page_service.advanced_search(search_phrase, **search_params)
        product_names = SearchPageService.get_product_names(products)

        assert not product_title in product_names, f'{product_title} is at the results list with unchecked search in descriptions checkbox.' \

    product_secription_search_data = ['A groundbreaking Retina display', 'dual-core', 'cor']

    @pytest.mark.tc77
    @pytest.mark.tc78
    @pytest.mark.tc79
    @pytest.mark.parametrize('search_data', product_secription_search_data)
    def test_verify_search_by_partial_description(self, search_page_service, search_data):
        
        product_title = 'Apple MacBook Pro 13-inch'

        search_params = {
            'search_in_description': True,
        }

        search_page_service.open_search_page()
        search_page_service.advanced_search(search_data, expected_product_name=product_title, **search_params) 

