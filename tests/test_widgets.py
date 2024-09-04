import time

import allure
import pytest

from data.links import URL
from pages.widgets_page import AccordionPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage, TabsPage


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

    @allure.feature('Date Picker')
    class TestDatePicker:
        @allure.description('Can change date in the date picker')
        def test_date_picker(self, driver):
            page = DatePickerPage(driver, URL.DATE_PICKER)
            page.open_page()

            date_value_before, date_value_after = page.select_random_date()
            assert date_value_before != date_value_after, 'The date has not be changed'

        @allure.description('Can change date and time in the date and time picker')
        def test_date_and_time_picker(self, driver):
            page = DatePickerPage(driver, URL.DATE_PICKER)
            page.open_page()

            date_value_before, date_value_after = page.select_random_date_and_time()
            assert date_value_before != date_value_after, 'The date and time have not be changed'

    @allure.feature('Slider')
    class TestSlider:
        @allure.description('Can move slider and change its value')
        def test_slider(self, driver):
            page = SliderPage(driver, URL.SLIDER)
            page.open_page()

            value_before, value_after = page.move_slider()
            assert value_before != value_after, 'The slider value has not been changed'

    @allure.feature('Progress Bar')
    class TestProgressBar:
        @allure.description('Progress bar value changes when moving')
        def test_change_progress_bar(self, driver):
            page = ProgressBarPage(driver, URL.PROGRESS_BAR)
            page.open_page()

            value_before, value_after = page.change_progress_bar_value()
            assert value_before != value_after, 'The progress bar value has not been changed'

        @allure.description('Start/Stop button name changes when clicking on it')
        def test_start_button_name_changes(self, driver):
            page = ProgressBarPage(driver, URL.PROGRESS_BAR)
            page.open_page()

            initial_button_name = page.click_start_button()
            button_name_after_one_click = page.click_start_button()
            button_name_after_two_clicks = page.click_start_button()

            assert initial_button_name == 'Start', 'Check initial button name'
            assert button_name_after_one_click == 'Stop', 'Check button name after one click'
            assert button_name_after_two_clicks == 'Start', 'Check button name after two clicks'

        @allure.description('Can reset the progress bar')
        def test_reset(self, driver):
            page = ProgressBarPage(driver, URL.PROGRESS_BAR)
            page.open_page()

            value_after_reset = page.check_reset()
            assert value_after_reset == '0'

    @allure.feature('Tabs')
    class TestTabs:
        @allure.description('Can switch between tabs, the tabs have content text')
        @pytest.mark.parametrize('tab_name', ['What', 'Origin', 'Use', 'More'])
        def test_tabs(self, driver, tab_name):
            page = TabsPage(driver, URL.TABS)
            page.open_page()

            what_tab_name, what_tab_content = page.check_tabs(tab_name)
            assert what_tab_name == tab_name and what_tab_content != 0, \
                f'"{tab_name}" tab name is not correct or missing content text'
