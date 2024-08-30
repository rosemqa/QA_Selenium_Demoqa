import time
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

    @allure.feature('Auto Complete')
    class TestAutoComplete:
        @allure.description('Can enter colors into the multi input field, all entered colors are displayed')
        def test_fill_multi_autocomplete(self, driver):
            page = AutoCompletePage(driver, URL.AUTO_COMPLETE)
            page.open_page()

            entered_colors = page.enter_multy_colors()
            colors_in_field = page.get_color_values_from_multi()

            assert entered_colors == colors_in_field, 'The entered color(s) missing in the input field'

        @allure.description('Can delete a color from multi input')
        def test_delete_color_from_multi(self, driver):
            page = AutoCompletePage(driver, URL.AUTO_COMPLETE)
            page.open_page()

            page.enter_multy_colors()
            page.delete_color_from_multi()
            color_count_before, color_count_after = page.delete_color_from_multi()

            assert color_count_before > color_count_after, 'Color was not deleted from multi input'

        @allure.description('Can delete all colors from multi input')
        def test_delete_all_colors_from_multi(self, driver):
            page = AutoCompletePage(driver, URL.AUTO_COMPLETE)
            page.open_page()

            page.enter_multy_colors()
            are_colors_present = page.delete_all_colors_from_multi()

            assert are_colors_present is False, 'Colors ware not deleted from multi input'

        @allure.description('Can fill the single autocomplete')
        def test_fill_single_autocomplete(self, driver):
            page = AutoCompletePage(driver, URL.AUTO_COMPLETE)
            page.open_page()

            entered_color = page.fill_single_input()
            color_in_field = page.get_color_value_from_single()

            assert entered_color == color_in_field, 'The entered color is missing in the input field'
