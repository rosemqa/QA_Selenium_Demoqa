from selenium.webdriver.common.by import By


class AccordionPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, '#section1Heading')
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, '#section1Content')
    SECOND_SECTION = (By.CSS_SELECTOR, '#section2Heading')
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, '#section2Content')
    THIRD_SECTION = (By.CSS_SELECTOR, '#section3Heading')
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, '#section3Content')


class AutoCompletePageLocators:
    MULTIPLE_COLOR_INPUT = (By.CSS_SELECTOR, '#autoCompleteMultipleInput')
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, '#autoCompleteSingleInput')
    MULTIPLE_COLOR_VALUE = (By.CSS_SELECTOR, '.auto-complete__multi-value__label')
    SINGLE_COLOR_VALUE = (By.CSS_SELECTOR, '.auto-complete__single-value')
    REMOVE_MULTIPLE_COLOR_ICON = (By.CSS_SELECTOR, '.auto-complete__multi-value__remove')
    REMOVE_ALL_MULTIPLE_COLORS_ICON = (By.CSS_SELECTOR, '.auto-complete__clear-indicator')
