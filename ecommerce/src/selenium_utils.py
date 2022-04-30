from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

class SeleniumUtils:

    def __init__(self, driver):
        self.driver = driver


    # def __get_timeout(self, timeout):
    #     timeout = timeout if timeout else self.default_timeout
    #     return timeout

    
    # def wait_and_input_text(self, locator, text, timeout=None):
    #     # time.sleep(2)
    #     # self.driver.find_
    #     WebDriverWait(self.driver, self.__get_timeout(timeout)).until(
    #         expected_conditions.visibility_of_element_located(locator)
    #     ).send_keys(text)
    
    
    # def wait_and_click_element(self, locator, timeout=None):
    #     WebDriverWait(self.driver, self.__get_timeout(timeout)).until(
    #         expected_conditions.visibility_of_element_located(locator)
    #     ).click()
    
    # def wait_for_text_in_element(self, locator, text, timeout=None):
    #     WebDriverWait(self.driver, self.__get_timeout(timeout)).until(
    #         expected_conditions.text_to_be_present_in_element(locator, text)
    #     )
    
    def wait_for_iframe_and_switch(self, locator, timeout=None):
        iframe = WebDriverWait(self.driver, self.__get_timeout(timeout)).until(
            expected_conditions.presence_of_element_located(locator)
        )
        self.driver.switch_to.frame(iframe)