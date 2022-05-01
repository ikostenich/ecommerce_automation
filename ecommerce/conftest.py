import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
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

    yield

    # driver.quit()