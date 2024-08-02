import os
import random
import time
import allure
import pytest
from data.links import URL
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.description('Info in the output form matches the input fields')
        def test_text_box(self, driver):
            page = TextBoxPage(driver, URL.TEXT_BOX)
            page.open_page()

            full_name, email, current_address, permanent_address = page.fill_all_fields()
            page.click_submit_button()
            output_fullname, output_email, output_current_address, output_permanent_address = page.get_output_form_info()

            assert output_fullname == full_name, 'Full name does not match'
            assert output_email == email, 'Email does not match'
            assert output_current_address == current_address, 'Current_address does not match'
            assert output_permanent_address == permanent_address, 'Permanent_address does not match'

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.description('Titles of ticked checkboxes match the output results')
        def test_check_boxes(self, driver):
            page = CheckBoxPage(driver, URL.CHECK_BOX)
            page.open_page()

            page.click_expand_all_button()
            page.click_random_checkboxes()
            input_checkbox = page.get_ticked_checkboxes_titles()
            output_result = page.get_output_result_text()

            with allure.step('Assert Input and Output results are the same'):
                assert input_checkbox == output_result, 'Titles of ticked checkboxes does not match the output results'

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.description('Name of ticked radiobutton match the output result')
        @pytest.mark.parametrize('button_name', ['Yes', 'Impressive', 'No'])
        def test_radio_button(self, driver, button_name):
            page = RadioButtonPage(driver, URL.RADIO_BUTTON)
            page.open_page()

            page.click_radio_button(button_name)
            output = page.get_output_result_text()

            assert output == button_name, f'Check output for {button_name}'

    @allure.feature('WebTable')
    class TestWebTable:
        @allure.description('Can add a new person to the table')
        def test_add_person_to_the_table(self, driver):
            page = WebTablePage(driver, URL.WEB_TABLE)
            page.open_page()

            new_person = page.add_new_person()
            table_data = page.get_table_data_text()

            assert new_person in table_data, 'A new person is not added to the table'

        @allure.description('Can search for a person in the table by keyword')
        def test_search_person_in_the_table(self, driver):
            page = WebTablePage(driver, URL.WEB_TABLE)
            page.open_page()

            keyword = page.add_new_person()[random.randint(0, 5)]
            page.enter_keyword_into_search_field(keyword)
            table_row = page.get_table_row_text()

            assert keyword in table_row, 'Person not found in table by keyword'

        @allure.description('Can edit person data in the table')
        def test_edit_person_data_in_the_table(self, driver):
            page = WebTablePage(driver, URL.WEB_TABLE)
            page.open_page()

            new_data = page.edit_person_data()
            table_row = page.get_table_row_text()

            assert new_data == table_row, 'Person data has not been changed'

        @allure.description('Can delete person from the table')
        def test_delete_person_in_the_table(self, driver):
            page = WebTablePage(driver, URL.WEB_TABLE)
            page.open_page()

            email = page.add_new_person()[3]
            page.enter_keyword_into_search_field(email)
            page.click_delete_button()
            text = page.get_no_rows_found_text()

            assert text == 'No rows found', 'Check "No rows found" text'

        @allure.description('Can change the number of rows in the table')
        def test_change_row_count_in_the_table(self, driver):
            row_count = [5, 10, 20, 25, 50, 100]

            page = WebTablePage(driver, URL.WEB_TABLE)
            page.open_page()

            assert page.change_row_count() == row_count, \
                'The number of rows in the table does not match the selected number'

    @allure.feature('Buttons')
    class TestButtons:
        @allure.description('Checking different types of clicks (double, right, left)')
        def test_different_click_types_on_the_buttons(self, driver, check):
            page = ButtonsPage(driver, URL.BUTTONS)
            page.open_page()

            double_click = page.click_on_different_buttons('double')
            right_click = page.click_on_different_buttons('right')
            left_click = page.click_on_different_buttons('click')

            with check:
                assert double_click == 'You have done a double click', 'Check message for double click'
            with check:
                assert right_click == 'You have done a right click', 'Check message for right click'
            assert left_click == 'You have done a dynamic click', 'Check message for left click'

    @allure.feature('Links')
    class TestLinks:
        @allure.description('Simple link opens a new tab and leads to relevant URL')
        def test_links(self, driver):
            page = LinksPage(driver, URL.LINKS)
            page.open_page()

            current_url, link_href = page.click_simple_link()

            assert link_href == current_url, f'Check link {link_href}'
            # assert current_url == 'https://demoqa.com/'

        @allure.description('Broken link returns correct status code')
        def test_broken_link(self, driver):
            page = LinksPage(driver, URL.LINKS)
            page.open_page()

            response_code = page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "Unexpected status code"

    @allure.feature('Upload and Download')
    class TestUploadDownload:
        @allure.description('Can upload a file')
        def test_upload_file(self, driver):
            page = UploadDownloadPage(driver, URL.UPLOAD_DOWNLOAD)
            page.open_page()

            file_name = page.upload_file()
            upload_result = page.get_upload_result_text()

            assert file_name == upload_result, 'Check file name in upload result'

        @allure.description('Can download a file')
        def test_download(self, driver):
            page = UploadDownloadPage(driver, URL.UPLOAD_DOWNLOAD)
            page.open_page()

            assert page.download_file() is True, 'The file was not downloaded'

    @allure.feature('Dynamic Properties')
    class TestDynamicProperties:
        @allure.description('Check if the "Enable" button will be enabled after 5 seconds')
        def test_dynamic_properties(self, driver):
            page = DynamicPropertiesPage(driver, URL.DYNAMIC_PROPERTIES)
            page.open_page()

            assert page.is_enable_button_enabled() is False, 'The initial state of the button is "enabled"'
            time.sleep(5)
            assert page.is_enable_button_enabled(), 'The button is not enabled after 5 seconds'

        @allure.description('Check if button text changes after 5 seconds')
        def test_change_button_color(self, driver):
            page = DynamicPropertiesPage(driver, URL.DYNAMIC_PROPERTIES)
            page.open_page()

            assert page.get_color_of_button_text() == '#ffffff', 'Initial button color is not correct'
            time.sleep(5)
            assert page.get_color_of_button_text() == '#dc3545', 'Final button color is not correct'

        @allure.description('Check if the "Visible" button appears after 5 seconds')
        def test_button_visible(self, driver):
            page = DynamicPropertiesPage(driver, URL.DYNAMIC_PROPERTIES)
            page.open_page()

            assert page.is_button_present() is False, 'The initial state of the button is "visible"'
            time.sleep(5)
            assert page.is_button_present(), 'The button does not appear after 5 seconds'
