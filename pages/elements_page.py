import allure
from faker import Faker

from data.generator import generated_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators


class ElementPage(BasePage):
    locators = TextBoxPageLocators()

    # GETTERS
    def get_output_name_text(self):
        return self.find_element(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]

    def get_output_email_text(self):
        return self.find_element(self.locators.OUTPUT_EMAIL).text.split(':')[1]

    def get_output_current_address_text(self):
        return self.find_element(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]

    def get_output_permanent_address_text(self):
        return self.find_element(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]

    def get_output_form_info(self):
        """get text from output form"""
        fullname = self.find_element(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        email = self.find_element(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.find_element(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.find_element(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return fullname, email, current_address, permanent_address

    # ACTIONS
    @allure.step('Enter fullname')
    def enter_fullname(self, fullname):
        self.find_element(self.locators.FULL_NAME).send_keys(fullname)
        # return self.fullname

    @allure.step('Enter Email')
    def enter_email(self, email):
        self.find_element(self.locators.EMAIL).send_keys(email)
        # return self.email

    @allure.step('Enter current address')
    def enter_current_address(self, current_address):
        self.find_element(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        # return self.current_address

    @allure.step('Enter permanent address')
    def enter_permanent_address(self, permanent_address):
        self.find_element(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        # return self.permanent_address

    @allure.step('Fill in all the fields')
    def fill_all_fields(self):
        person_info = generated_person()
        fullname = person_info.fullname
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('Enter fullname'):
            self.find_element(self.locators.FULL_NAME).send_keys(fullname)
        with allure.step('Enter Email'):
            self.find_element(self.locators.EMAIL).send_keys(email)
        with allure.step('Enter current_address'):
            self.find_element(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        with allure.step('Enter permanent_address'):
            self.find_element(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return fullname, email, current_address, permanent_address

    @allure.step('Click Submit button')
    def click_submit_button(self):
        self.find_element(self.locators.SUBMIT_BUTTON).click()

