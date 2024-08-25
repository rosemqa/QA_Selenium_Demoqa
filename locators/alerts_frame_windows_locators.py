from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, '#tabButton')
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE_BTN = (By.CSS_SELECTOR, '#messageWindowButton')
    NEW_TAB_TITLE_TEXT = (By.CSS_SELECTOR, '#sampleHeading')
