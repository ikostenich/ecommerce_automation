from selenium.webdriver.common.by import By


class SearchBarLocators:

    SEARCH_FIELD = (By.ID, 'small-searchterms')
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'search-box-button')]")
