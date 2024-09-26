import allure
import os
import random
import time
from datetime import datetime
from selenium.webdriver import Keys
from data.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = FormPageLocators
    subjects = [  # subjects found in dev tools > sources > demoqa.com > bundle.js
        'English',
        'Maths',
        'Physics',
        'Chemistry',
        'Biology',
        'Computer Science',
        'Accounting',
        'Economics',
        'Hindi',
        'Arts',
        'Social Studies',
        'History',
        'Civics'
    ]

    states = [
        'NCR',
        'Uttar',
        'Haryana',
        'Rajasthan'
    ]

    @allure.step('Get results from  the results table')
    def get_result_table_info(self):
        time.sleep(1)
        output_results = self.find_elements(self.locators.TABLE_RESULTS)
        output_results_values = [i.text for i in output_results]
        return output_results_values

    def get_state_text(self):
        return self.find_element(self.locators.SELECT_STATE_DROPDOWN).text

    def get_city_text(self):
        return self.find_element(self.locators.SELECT_CITY_DROPDOWN).text

    @allure.step('Fill out the form and click Submit button')
    def fill_form(self):
        person_info = generated_person()
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        phone_number = person_info.phone_number[:10]
        current_address = person_info.current_address
        file_path = generated_file()
        subject = random.choice(self.subjects)
        state = random.choice(self.states)
        random_gender = self.find_element(self.locators.GENDER_RADIOBUTTON)
        random_hobby = self.find_element(self.locators.HOBBIES_CHECKBOX)

        date = self.find_element(self.locators.DATE).get_attribute('value')  # строка с датой
        # преобразуем строку в объект datetime, указывая формат '%d %b %Y' (день Ммм год)
        date_obj = datetime.strptime(date, '%d %b %Y')
        # преобразуем объект datetime обратно в строку с нужным форматом (день месяц_полностью,год)
        formatted_date = date_obj.strftime('%d %B,%Y')

        with allure.step('Enter first name'):
            self.find_element(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        with allure.step('Enter last name'):
            self.find_element(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        with allure.step('Enter email'):
            self.find_element(self.locators.EMAIL_INPUT).send_keys(email)
        with allure.step('Select gender'):
            random_gender.click()
            selected_gender = random_gender.text
        with allure.step('Enter phone number'):
            self.find_element(self.locators.PHONE_NUMBER_INPUT).send_keys(phone_number)
        with allure.step('Enter subject/select subject'):
            self.find_element(self.locators.SUBJECT_FIELD).send_keys(subject)
            self.find_element(self.locators.SUBJECT_FIELD).send_keys(Keys.ENTER)
        with allure.step('Select a hobby'):
            random_hobby.click()
            selected_hobby = random_hobby.text
        with allure.step('Upload file'):
            self.find_element(FormPageLocators.UPLOAD_FILE).send_keys(file_path)
            os.remove(file_path)
        with allure.step('Enter address'):
            self.find_element(self.locators.ADDRESS_INPUT).send_keys(current_address)
        with allure.step('Select a random state'):
            self.find_element(self.locators.STATE_INPUT).send_keys(state)
            self.find_element(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        with allure.step('Select a random city'):
            self.find_element(self.locators.SELECT_CITY_DROPDOWN).click()
            self.find_element(self.locators.CITY_INPUT).send_keys(Keys.DOWN * random.randint(0, 2))
            self.find_element(self.locators.CITY_INPUT).send_keys(Keys.ENTER)
        with allure.step('Click Submit button'):
            self.find_element(self.locators.SUBMIT_BUTTON).click()
        return [
            f'{first_name} {last_name}',
            email,
            selected_gender,
            phone_number,
            formatted_date,
            subject,
            selected_hobby,
            file_path.replace('\\', '/').split('/')[-1],
            current_address,
            f'{self.get_state_text()} {self.get_city_text()}'
        ]
