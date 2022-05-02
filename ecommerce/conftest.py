import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ecommerce.src.pages.home_page import HomePage 
from ecommerce.src.services.search_page_service import SearchPageService   

@pytest.fixture(scope='class')
def driver(request):

    browsers = ['chrome', 'headlesschrome']

    browser = os.environ.get('BROWSER', 'chrome')    

    if browser.lower() not in browsers:
        raise Exception(f'Provided browser "{browser}" is not supported')

    chrome_options = Options()
    # chrome_options.add_argument("--start-fullscreen")
    if browser == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'headlesschrome':
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    
    request.cls.driver = driver


    home_page = HomePage(request.cls.driver)
    home_page.open_home_page()

    yield request.cls.driver

    driver.quit()


@pytest.fixture(scope='class')
def search_page_service(driver):

    search_page_service = SearchPageService(driver)

    yield search_page_service


@pytest.fixture(scope='function')
def open_search_page(search_page_service):

    search_page_service.page.open_search_page()

    yield