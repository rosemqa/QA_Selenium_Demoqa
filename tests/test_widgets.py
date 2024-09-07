import time
import allure
import pytest
from data.links import URL
from pages.widgets_page import AccordionPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


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

    @allure.feature('Tool Tips')
    class TestToolTips:
        tool_tips = [
            ('button', 'You hovered over the Button'),
            ('text_field', 'You hovered over the text field'),
            ('contrary_link', 'You hovered over the Contrary'),
            ('section_link', 'You hovered over the 1.10.32')
        ]

        @allure.description('Check the tool tips text')
        @pytest.mark.parametrize('hover_element, expected_text', tool_tips)
        def test_tool_tips(self, driver, hover_element, expected_text):
            page = ToolTipsPage(driver, URL.TOOL_TIPS)
            page.open_page()

            toll_tip_text = page.get_toll_tip_text(hover_element)
            assert toll_tip_text == expected_text, f'Check tool tip text for "{hover_element}" element'

    @allure.feature('Menu')
    class TestMenu:
        @allure.description('Can open the menu/submenu, menu items have correct names')
        def test_menu(self, driver):
            expected_item_names = [
                'Main Item 1',
                'Main Item 2',
                'Sub Item',
                'Sub Item',
                'SUB SUB LIST »',
                'Sub Sub Item 1',
                'Sub Sub Item 2',
                'Main Item 30'
            ]
            page = MenuPage(driver, URL.MENU)
            page.open_page()

            menu_items = page.get_menu_items_names()
            assert menu_items == expected_item_names, 'Check names of the menu items'

    @allure.feature('Select Menu')
    class TestSelectMenu:

        @allure.description('Can select a title in the "Select One" menu')
        def test_select_one_menu(self, driver):
            page = SelectMenuPage(driver, URL.SELECT_MENU)
            page.open_page()

            entered_title = page.select_title()
            field_value = page.get_value_from_title_field()
            assert entered_title == field_value, 'The entered title is missing in the input field'

        @allure.description('Can select colors in "Multiselect drop down", all selected colors are displayed')
        def test_multiselect_menu(self, driver):
            page = SelectMenuPage(driver, URL.SELECT_MENU)
            page.open_page()

            entered_colors = page.select_multiple_colors()
            field_values = page.get_values_from_multiselect_field()
            assert entered_colors == field_values, 'The entered colors are missing in the input field'

        @allure.description('Check that expected colors are present in Old Style Select Menu')
        def test_old_style_select(self, driver, check):
            expected_color_list = ['Red', 'Blue', 'Green']

            page = SelectMenuPage(driver, URL.SELECT_MENU)
            page.open_page()

            color_list = page.get_values_from_old_style_select()
            for color in expected_color_list:
                with check:
                    assert color in color_list, f'{color} color is missing in the Dropdown'
