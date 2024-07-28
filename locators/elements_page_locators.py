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
    CHECKBOX_TITLE = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')


class RadioButtonPageLocators:
    YES_RADIO_BTN = (By.CSS_SELECTOR, '[for="yesRadio"]')
    IMPRESSIVE_RADIO_BTN = (By.CSS_SELECTOR, '[for="impressiveRadio"]')
    NO_RADIO_BTN = (By.CSS_SELECTOR, '[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')


class WebTablePAgeLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#searchBox')
    # ADD PERSON FORM
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#lastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#userEmail')
    AGE_FIELD = (By.CSS_SELECTOR, '#age')
    SALARY_FIELD = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT = (By.CSS_SELECTOR, '#department')
    SUBMIT_BTN = (By.CSS_SELECTOR, '#submit')
    # TABLE
    EDIT_BTN = (By.CSS_SELECTOR, '[title="Edit"]')
    DELETE_BTN = (By.CSS_SELECTOR, '[title="Delete"]')
    TABLE_ROW = (By.CSS_SELECTOR, '[role="rowgroup"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, '.rt-noData')
    ROW_COUNT_DROPDOWN = (By.CSS_SELECTOR, '[aria-label="rows per page"]')
