from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, driver, locator, default_timeout=10):
        self.driver = driver
        self.locator = locator
        self.default_timeout = default_timeout
        self.web_element = None
        self.find()

    def __get_timeout(self, timeout):
        timeout = timeout if timeout else self.default_timeout
        return timeout

    
    def find(self, timeout=None):
        element = WebDriverWait(
            self.driver, self.__get_timeout(timeout)
            ).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element

    def click(self, timeout=None):
        element = WebDriverWait(
            self.driver, self.__get_timeout(timeout)
            ).until(EC.element_to_be_clickable(self.locator))
        element.click()
    
    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
    
    @property
    def is_displayed(self):        
        return self.web_element.is_displayed()
    
    @property
    def text(self):
        text = self.web_element.text
        return text
    
    @property
    def element(self):
        return self.web_element