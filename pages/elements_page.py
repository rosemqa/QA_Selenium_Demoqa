import os
import random
import time

import allure
import requests
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

from data.data import DOWNLOAD_DIR
from data.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePAgeLocators, ButtonsPageLocators, LinksPageLocators, UploadDownloadPageLocators, \
    DynamicPropertiesPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def get_output_form_info(self):
        """get text from output form"""
        fullname = self.find_element(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        email = self.find_element(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.find_element(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.find_element(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return fullname, email, current_address, permanent_address

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
            time.sleep(1)
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


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators

    @allure.step('Get output message text on click')
    def get_output_msg_on_click(self, locator):
        return self.find_element(locator).text

    def click_on_different_buttons(self, click_type):
        if click_type == 'double':
            with allure.step('Double click the Double Click Me button'):
                self.double_click(self.locators.DOUBLE_CLICK_ME_BTN)
                return self.get_output_msg_on_click(self.locators.DOUBLE_CLICK_MSG)
        elif click_type == 'right':
            with allure.step('Right click the Right Click Me button'):
                self.right_click(self.locators.RIGHT_CLICK_BTN)
                return self.get_output_msg_on_click(self.locators.RIGHT_CLICK_MSG)
        elif click_type == 'click':
            with allure.step('Click the Click Me button'):
                self.find_element(self.locators.CLICK_ME_BTN).click()
                return self.get_output_msg_on_click(self.locators.DYNAMIC_CLICK_MSG)


class LinksPage(BasePage):
    locators = LinksPageLocators

    @allure.step('Click simple link')
    def click_simple_link(self):
        simple_link = self.find_element(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        response = requests.get(link_href)
        assert response.status_code == 200, f'Link "{link_href}" returns status code {response.status_code}'
        simple_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        return url, link_href

    @allure.step('Check_ broken link')
    def check_broken_link(self, url):
        response = requests.get(url)
        assert response.status_code != 200, f'The link {url} works, status code is 200'
        # if response.status_code == 200:
        #     self.find_element(self.locators.BAD_REQUEST_LINK).click()
        #     return response.status_code
        # else:
        return response.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators

    @allure.step('Get file name in the upload result')
    def get_upload_result_text(self):
        return self.find_element(self.locators.UPLOAD_RESULT).text.split('\\')[-1]

    @allure.step('Upload file')
    def upload_file(self):
        file_path = generated_file()
        self.find_element(self.locators.UPLOAD_FILE).send_keys(file_path)
        os.remove(file_path)  # removes file
        return file_path.split('\\')[-1]  # returns file name

    @allure.step('Download file')
    def download_file(self):
        file_name = self.find_element(self.locators.DOWNLOAD_BTN).get_attribute('download')
        file_path = os.path.join(DOWNLOAD_DIR, file_name)
        self.find_element(self.locators.DOWNLOAD_BTN).click()
        time.sleep(2)
        check_file = os.path.isfile(file_path)  # проверка что объект cуществует и является файлом (не директорией)
        if os.path.isfile(file_path):
            os.remove(file_path)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators

    @allure.step('Get css color value for button text')
    def get_color_of_button_text(self):
        # GET COLOR IN RGB FORMAT
        css_color_value = self.find_element(self.locators.COLOR_CHANGE_BTN).value_of_css_property('color')
        # CONVERT RGB TO HEX FORMAT
        hex_color = Color.from_string(css_color_value).hex
        return hex_color

    @allure.step('Check if the "Enable" button is enabled')
    def is_enable_button_enabled(self):
        return self.find_visible_element(self.locators.WILL_ENABLE_BTN).is_enabled()

    @allure.step('Check if "Visible" button is present/visible')
    def is_button_present(self):
        return self.is_element_present(self.locators.VISIBLE_AFTER_BTN, timeout=1)
