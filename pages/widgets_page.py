import time
import allure
from locators.widgets_page_locators import AccordionPageLocators
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
