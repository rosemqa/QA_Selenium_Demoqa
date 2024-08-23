import allure
from data.links import URL
from pages.form_page import PracticeFormPage


@allure.suite('Forms')
class TestForms:
    @allure.feature('Practice Form')
    class TestPracticeForm:
        @allure.description('Can fill out and submit the form and get the correct results in the results table')
        def test_practice_form(self, driver):
            page = PracticeFormPage(driver, URL.FORMS)
            page.open_page()

            inp = page.fill_form()
            output = page.get_result_table_info()

            assert inp == output, 'The data entered in the form and the results in the table are different'
