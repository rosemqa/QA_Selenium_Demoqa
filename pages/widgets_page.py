import random
import time
import allure
from selenium.webdriver import Keys

from locators.widgets_page_locators import AccordionPageLocators, AutoCompletePageLocators
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
