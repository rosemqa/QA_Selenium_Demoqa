from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # FORM FIELDS
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    # OUTPUT FORM
    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, '#name')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, '#email')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p#currentAddress')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p#permanentAddress')

