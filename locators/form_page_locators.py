import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    GENDER_RADIOBUTTON = (By.CSS_SELECTOR, f'[for="gender-radio-{random.randint(1, 3)}"]')
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, '#userNumber')
    DATE = (By.CSS_SELECTOR, '#dateOfBirthInput')
    SUBJECT_FIELD = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES_CHECKBOX = (By.CSS_SELECTOR, f'[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, '#uploadPicture')
    ADDRESS_INPUT = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE_DROPDOWN = (By.CSS_SELECTOR, '#state')
    STATE_INPUT = (By.CSS_SELECTOR, '#react-select-3-input')
    SELECT_CITY_DROPDOWN = (By.CSS_SELECTOR, '#city')
    CITY_INPUT = (By.CSS_SELECTOR, '#react-select-4-input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    TABLE_RESULTS = (By.XPATH, '//td[2]')
