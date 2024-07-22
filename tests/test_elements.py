import time
import allure
from data.links import URL
from pages.elements_page import ElementPage


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.description('Info in the output form matches the input fields')
        def test_text_box(self, driver):
            page = ElementPage(driver, URL.TEXT_BOX)
            page.open_page()

            full_name, email, current_address, permanent_address = page.fill_all_fields()
            page.click_submit_button()
            output_fullname, output_email, output_current_address, output_permanent_address = page.get_output_form_info()

            assert output_fullname == full_name, 'Full name does not match'
            assert output_email == email, 'Email does not match'
            assert output_current_address == current_address, 'Current_address does not match'
            assert output_permanent_address == permanent_address, 'Permanent_address does not match'
