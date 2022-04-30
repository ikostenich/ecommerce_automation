from selenium.webdriver.common.by import By


class BasePageLocators:

    IFRAME_LOCATOR = (By.XPATH, "//iframe[@src]")
    # WELCOME_BLOCK_TITLE = (By.XPATH, '//div[@class="topic-block-title"]//h2')
