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


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, '#datePickerMonthYearInput')
    DATE_MONTH_DROPDOWN = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    DATE_YEAR_DROPDOWN = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    DATE_DAY = (By.CSS_SELECTOR, '.react-datepicker__day')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, '#dateAndTimePickerInput')
    DATE_AND_TIME_MONTH_DROPDOWN = (By.CSS_SELECTOR, '.react-datepicker__month-read-view')
    DATE_AND_TIME_YEAR_DROPDOWN = (By.CSS_SELECTOR, '.react-datepicker__year-read-view')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, '.react-datepicker__month-option')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, '.react-datepicker__year-option')
    DATE_AND_TIME_TIME = (By.CSS_SELECTOR, '.react-datepicker__time-list-item')
