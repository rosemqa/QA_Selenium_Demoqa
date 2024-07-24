import time
import allure
from data.links import URL
from pages.elements_page import TextBoxPage, CheckBoxPage


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

            with (allure.step('Assert Input and Output results are the same')):
                assert input_checkbox == output_result, 'Titles of ticked checkboxes does not match the output results'
