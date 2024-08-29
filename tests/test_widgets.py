import allure
from data.links import URL
from pages.widgets_page import AccordionPage, AutoCompletePage


@allure.suite('Widgets')
class TestWidgets:
    @allure.feature('Accordion')
    class TestAccordion:
        @allure.description('Accordion sections can be expanded/collapsed')
        def test_accordion(self, driver):
            page = AccordionPage(driver, URL.ACCORDIAN)
            page.open_page()

            assert page.is_first_content_displayed() is True, 'First section is initially collapsed'
            page.click_second_section_title()
            assert page.is_first_content_displayed() is False, \
                'First section content is still displayed after clicking the second section title'
            assert page.is_second_content_displayed() is True, \
                'Second section content is not displayed after clicking the second section title'
            page.click_third_section_title()
            assert page.is_second_content_displayed() is False, \
                'Second section content is still displayed after clicking the third section title'
            assert page.is_third_content_displayed() is True, \
                'Third section content is not displayed after clicking the third section title'
            page.click_third_section_title()
            assert page.is_third_content_displayed() is False, \
                'Third section content is still displayed after clicking the third section title'

    class TestAutoComplete:
        def test_auto_complete(self, driver):
            page = AutoCompletePage(driver, URL.AUTO_COMPLETE)
            page.open_page()



