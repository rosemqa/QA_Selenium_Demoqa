import random
import allure
from selenium.webdriver.support.select import Select
from data.generator import generated_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePAgeLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    # GETTERS
    # def get_output_name_text(self):
    #     return self.find_element(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
    #
    # def get_output_email_text(self):
    #     return self.find_element(self.locators.OUTPUT_EMAIL).text.split(':')[1]
    #
    # def get_output_current_address_text(self):
    #     return self.find_element(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
    #
    # def get_output_permanent_address_text(self):
    #     return self.find_element(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]

    def get_output_form_info(self):
        """get text from output form"""
        fullname = self.find_element(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        email = self.find_element(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.find_element(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.find_element(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return fullname, email, current_address, permanent_address

    # ACTIONS
    # @allure.step('Enter fullname')
    # def enter_fullname(self, fullname):
    #     self.find_element(self.locators.FULL_NAME).send_keys(fullname)
    #     # return self.fullname
    #
    # @allure.step('Enter Email')
    # def enter_email(self, email):
    #     self.find_element(self.locators.EMAIL).send_keys(email)
    #     # return self.email
    #
    # @allure.step('Enter current address')
    # def enter_current_address(self, current_address):
    #     self.find_element(self.locators.CURRENT_ADDRESS).send_keys(current_address)
    #     # return self.current_address
    #
    # @allure.step('Enter permanent address')
    # def enter_permanent_address(self, permanent_address):
    #     self.find_element(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
    #     # return self.permanent_address

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


class CheckBoxPage(BasePage):
    # GETTERS
    @allure.step('Get the text of the titles of ticked checkboxes')
    def get_ticked_checkboxes_titles(self):
        ticked_checkbox_list = self.find_elements(CheckBoxPageLocators.TICKED_CHECKBOX)
        checkbox_title_list = []
        for ticked_checkbox in ticked_checkbox_list:
            checkbox_title = ticked_checkbox.find_element(*CheckBoxPageLocators.CHECKBOX_TITLE).text.lower()
            checkbox_title_list.append(checkbox_title)
        return str(checkbox_title_list).replace(' ', '').replace('.doc', '')

    @allure.step('Get output result text')
    def get_output_result_text(self):
        output_result_list = self.find_elements(CheckBoxPageLocators.OUTPUT_RESULT)
        result_text_list = []
        for i in output_result_list:
            result_text_list.append(i.text.lower())
        return str(result_text_list).replace(' ', '').replace('.doc', '')

    # ACTIONS
    @allure.step('Click Expand All button')
    def click_expand_all_button(self):
        self.find_element(CheckBoxPageLocators.EXPAND_ALL_BTN).click()

    @allure.step('Click several random checkboxes')
    def click_random_checkboxes(self):
        checkbox_list = self.find_elements(CheckBoxPageLocators.CHECKBOX)

        for _ in range(10):
            random_checkbox = checkbox_list[random.randint(0, 16)]
            random_checkbox.click()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators

    @allure.step('Get output result')
    def get_output_result_text(self):
        return self.find_element(self.locators.OUTPUT_RESULT).text

    def click_radio_button(self, choice):
        choices = {
            'Yes': self.locators.YES_RADIO_BTN,
            'Impressive': self.locators.IMPRESSIVE_RADIO_BTN,
            'No': self.locators.NO_RADIO_BTN
        }
        with allure.step(f'Click "{choice}" radio button'):
            self.find_element(choices[choice]).click()


class WebTablePage(BasePage):
    locators = WebTablePAgeLocators

    @allure.step('Get text from table data')
    def get_table_data_text(self):
        row_list = self.find_elements(self.locators.TABLE_ROW)
        return [row.text.split() for row in row_list]

    @allure.step('Get the text of the first row of the table')
    def get_table_row_text(self):
        return self.find_element(self.locators.TABLE_ROW).text.splitlines()

    @allure.step('Get "no rows found" text')
    def get_no_rows_found_text(self):
        return self.find_element(self.locators.NO_ROWS_FOUND).text

    @allure.step('Get number of rows in the table')
    def get_table_length_value(self):
        return len(self.find_elements(self.locators.TABLE_ROW))

    @allure.step('Add a new person to the table')
    def add_new_person(self):
        person_info = generated_person()
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        with allure.step('Click Add button'):
            self.find_element(self.locators.ADD_BUTTON).click()
        with allure.step('Fill in all the fields'):
            self.find_element(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
            self.find_element(self.locators.LAST_NAME_FIELD).send_keys(last_name)
            self.find_element(self.locators.EMAIL_FIELD).send_keys(email)
            self.find_element(self.locators.AGE_FIELD).send_keys(age)
            self.find_element(self.locators.SALARY_FIELD).send_keys(salary)
            self.find_element(self.locators.DEPARTMENT).send_keys(department)
        with allure.step('Click Submit button'):
            self.find_element(self.locators.SUBMIT_BTN).click()

        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Enter keyword into search field')
    def enter_keyword_into_search_field(self, keyword):
        self.find_element(self.locators.SEARCH_FIELD).send_keys(keyword)

    @allure.step('Edit person data in the table')
    def edit_person_data(self):
        person_info = generated_person()
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        with allure.step('Click Edit button'):
            self.find_element(self.locators.EDIT_BTN).click()
        with allure.step('Clear old data and enter new data'):
            self.find_element(self.locators.FIRST_NAME_FIELD).clear()
            self.find_element(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
            self.find_element(self.locators.LAST_NAME_FIELD).clear()
            self.find_element(self.locators.LAST_NAME_FIELD).send_keys(last_name)
            self.find_element(self.locators.EMAIL_FIELD).clear()
            self.find_element(self.locators.EMAIL_FIELD).send_keys(email)
            self.find_element(self.locators.AGE_FIELD).clear()
            self.find_element(self.locators.AGE_FIELD).send_keys(age)
            self.find_element(self.locators.SALARY_FIELD).clear()
            self.find_element(self.locators.SALARY_FIELD).send_keys(salary)
            self.find_element(self.locators.DEPARTMENT).clear()
            self.find_element(self.locators.DEPARTMENT).send_keys(department)
        with allure.step('Click Submit button'):
            self.find_element(self.locators.SUBMIT_BTN).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Click Delete button')
    def click_delete_button(self):
        self.find_element(self.locators.DELETE_BTN).click()

    @allure.step('Change the number of table rows')
    def change_row_count(self):
        row_count = ['5', '10', '20', '25', '50', '100']
        table_length = []
        for i in row_count:
            Select(self.find_element(self.locators.ROW_COUNT_DROPDOWN)).select_by_value(i)
            table_length.append(self.get_table_length_value())
        return table_length
