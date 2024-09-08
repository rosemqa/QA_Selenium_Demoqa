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


class SliderPageLocators:
    SLIDER_HANDLE = (By.CSS_SELECTOR, '.range-slider ')
    SLIDER_VALUE_BOX = (By.CSS_SELECTOR, '#sliderValue')


class ProgressBarPageLocators:
    START_BTN = (By.CSS_SELECTOR, '#startStopButton')
    RESET_BTN = (By.CSS_SELECTOR, '#resetButton')
    PROGRESS_BAR = (By.CSS_SELECTOR, '.progress-bar')


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, '#demo-tab-what')
    ORIGIN_TAB = (By.CSS_SELECTOR, '#demo-tab-origin')
    USE_TAB = (By.CSS_SELECTOR, '#demo-tab-use')
    MORE_TAB = (By.CSS_SELECTOR, '#demo-tab-more')

    WHAT_TAB_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-what')
    ORIGIN_TAB_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-origin')
    USE_TAB_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-use')
    MORE_TAB_CONTENT = (By.CSS_SELECTOR, '#demo-tabpane-more')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, '#toolTipButton')
    TEXT_FIELD = (By.CSS_SELECTOR, '#toolTipTextField')
    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')

    TOOL_TIP = (By.CSS_SELECTOR, '.tooltip-inner')


class MenuPageLocators:
    MENU_ITEM = (By.CSS_SELECTOR, 'li a')


class SelectMenuLocators:
    SELECT_VALUE_INPUT = (By.CSS_SELECTOR, '#withOptGroup input')
    SELECT_ONE_INPUT = (By.CSS_SELECTOR, '#selectOne input')
    SELECT_ONE_VALUE = (By.CSS_SELECTOR, '.css-1uccc91-singleValue')
    OLD_STYLE_SELECT = (By.CSS_SELECTOR, '#oldSelectMenu')
    MULTISELECT_INPUT = (By.XPATH, '(//input)[3]')
    MULTISELECT_ITEM_VALUE = (By.CSS_SELECTOR, '.css-12jo7m5')
    MULTISELECT_REMOVE_ITEM_ICON = (By.CSS_SELECTOR, '.css-xb97g8')
    MULTISELECT_CLEAR_ICON = (By.CSS_SELECTOR, 'div.css-1gtu0rj-indicatorContainer:nth-child(1)>svg')
