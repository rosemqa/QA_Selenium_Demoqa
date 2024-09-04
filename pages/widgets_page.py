import random
import time
import allure
from selenium.webdriver import Keys
from data.generator import generated_date
from locators.widgets_page_locators import AccordionPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    ProgressBarPageLocators, SliderPageLocators
from pages.base_page import BasePage


class AccordionPage(BasePage):
    locators = AccordionPageLocators

    @allure.step('Click the first section title')
    def click_first_section_title(self):
        self.find_element(self.locators.FIRST_SECTION).click()

    @allure.step('Click the second section title')
    def click_second_section_title(self):
        self.find_element(self.locators.SECOND_SECTION).click()

    @allure.step('Click the third section title')
    def click_third_section_title(self):
        self.find_element(self.locators.THIRD_SECTION).click()

    @allure.step('Check if content of the first section is displayed (is the first section collapsed)')
    def is_first_content_displayed(self):
        time.sleep(1)
        return self.is_element_present(self.locators.FIRST_SECTION_CONTENT, 1)

    @allure.step('Check if content of the second section is displayed (is the second section collapsed)')
    def is_second_content_displayed(self):
        time.sleep(1)
        return self.is_element_present(self.locators.SECOND_SECTION_CONTENT, 1)

    @allure.step('Check if content of the third section is displayed (is the third section collapsed)')
    def is_third_content_displayed(self):
        time.sleep(1)
        return self.is_element_present(self.locators.THIRD_SECTION_CONTENT, 1)


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]

    @allure.step('Get color values from multiple color input field')
    def get_color_values_from_multi(self):
        color_list = self.find_elements(self.locators.MULTIPLE_COLOR_VALUE)
        return [color.text for color in color_list]

    @allure.step('Get color value from single color input field')
    def get_color_value_from_single(self):
        return self.find_element(self.locators.SINGLE_COLOR_VALUE).text

    @allure.step('Enter several (2-10) random colors into the multiple color input field')
    def enter_multy_colors(self):
        colors = random.sample(self.colors, k=random.randint(2, 10))
        for color in colors:
            multi_input = self.find_element(self.locators.MULTIPLE_COLOR_INPUT)
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.ENTER)
        return colors

    @allure.step('Delete one color from multiple color input field')
    def delete_color_from_multi(self):
        color_count_before = len(self.find_elements(self.locators.MULTIPLE_COLOR_VALUE))
        self.find_element(self.locators.REMOVE_MULTIPLE_COLOR_ICON).click()
        color_count_after = len(self.find_elements(self.locators.MULTIPLE_COLOR_VALUE))
        return color_count_before, color_count_after

    @allure.step('Delete all colors from multi input, check that input field is blank')
    def delete_all_colors_from_multi(self):
        self.find_element(self.locators.REMOVE_ALL_MULTIPLE_COLORS_ICON).click()
        are_colors_present = self.is_element_present(self.locators.MULTIPLE_COLOR_VALUE, 0)
        return are_colors_present

    @allure.step('Enter a random color into the single color input field')
    def fill_single_input(self):
        color = random.choice(self.colors)
        self.find_element(self.locators.SINGLE_COLOR_INPUT).send_keys(color)
        self.find_element(self.locators.SINGLE_COLOR_INPUT).send_keys(Keys.ENTER)
        return color


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators

    @allure.step('Select month, year and day in the date picker')
    def select_random_date(self):
        date = generated_date()
        day = str(int(date.day))
        date_input = self.find_element(self.locators.DATE_INPUT)
        date_value_before = date_input.get_attribute('value')
        date_input.click()
        self.select_item_in_dropdown_by_text(self.locators.DATE_MONTH_DROPDOWN, date.month)
        self.select_item_in_dropdown_by_text(self.locators.DATE_YEAR_DROPDOWN, date.year)
        self.select_element_in_list_by_text(self.locators.DATE_DAY, day)
        date_value_after = date_input.get_attribute('value')
        return date_value_before, date_value_after

    @allure.step('Select month, year, day and time in the date and time picker')
    def select_random_date_and_time(self):
        date = generated_date()
        random_month = date.month
        random_day = str(int(date.day))
        random_time = date.time[:3] + random.choice(['00', '15', '30', '45'])
        date_input = self.find_element(self.locators.DATE_AND_TIME_INPUT)
        date_value_before = date_input.get_attribute('value')
        date_input.click()
        self.find_element(self.locators.DATE_AND_TIME_MONTH_DROPDOWN).click()
        self.select_element_in_list_by_text(self.locators.DATE_AND_TIME_MONTH, random_month)
        self.find_element(self.locators.DATE_AND_TIME_YEAR_DROPDOWN).click()
        random_year = self.find_elements(self.locators.DATE_AND_TIME_YEAR)[random.randint(1, 11)].text
        self.select_element_in_list_by_text(self.locators.DATE_AND_TIME_YEAR, random_year)
        self.select_element_in_list_by_text(self.locators.DATE_DAY, random_day)
        self.select_element_in_list_by_text(self.locators.DATE_AND_TIME_TIME, random_time)
        date_value_after = date_input.get_attribute('value')
        return date_value_before, date_value_after


class SliderPage(BasePage):
    locators = SliderPageLocators

    @allure.step('Move the slider to the right or left')
    def move_slider(self):
        value_before = self.find_element(self.locators.SLIDER_VALUE_BOX).get_attribute('value')
        slider_handle = self.find_element(self.locators.SLIDER_HANDLE)
        self.drag_and_drop_by_offset(slider_handle, random.randint(-150, 150), 0)
        value_after = self.find_element(self.locators.SLIDER_VALUE_BOX).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators

    @allure.step('Start/stop progress bar to change its value')
    def change_progress_bar_value(self):
        value_before = self.find_present_element(self.locators.PROGRESS_BAR).get_attribute('aria-valuenow')
        self.click_start_button()
        time.sleep(random.randint(3, 6))
        self.click_start_button()
        value_after = self.find_element(self.locators.PROGRESS_BAR).get_attribute('aria-valuenow')
        return value_before, value_after

    @allure.step('Click Start/Stop button and get button name')
    def click_start_button(self):
        start_button = self.find_element(self.locators.START_BTN)
        button_text = start_button.text
        start_button.click()
        return button_text

    @allure.step('Fill the progress bar, click Reset button, get the progress bar value')
    def check_reset(self):
        self.click_start_button()
        time.sleep(10)
        self.find_element(self.locators.RESET_BTN).click()
        value_after_reset = self.find_present_element(self.locators.PROGRESS_BAR).get_attribute('aria-valuenow')
        return value_after_reset
