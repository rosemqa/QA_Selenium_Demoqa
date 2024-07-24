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


class CheckBoxPageLocators:
    EXPAND_ALL_BTN = (By.CSS_SELECTOR, '.rct-icon-expand-all')
    CHECKBOX = (By.CSS_SELECTOR, '.rct-checkbox')
    TICKED_CHECKBOX = (By.CSS_SELECTOR, '.rct-icon-check')
    # CHECKBOX_TITLE = (By.XPATH, "/../../*[@class='rct-title")
    CHECKBOX_TITLE = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')


class RadioButtonPageLocators:
    YES_RADIO_BTN = (By.CSS_SELECTOR, '[for="yesRadio"]')
    IMPRESSIVE_RADIO_BTN = (By.CSS_SELECTOR, '[for="impressiveRadio"]')
    NO_RADIO_BTN = (By.CSS_SELECTOR, '[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')
