import time
import allure
import pytest
from data.links import URL
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable elements')
    class TestSortablePage:
        @allure.description('Can change the order of the List/Grid')
        @pytest.mark.parametrize('tab', ['list', 'grid'])
        def test_change_items_order(self, driver, tab):
            page = SortablePage(driver, URL.SORTABLE)
            page.open_page()

            order_before, order_after = page.change_items_order(tab)
            assert order_before != order_after, f'The order of the {tab} was not changed'

    @allure.feature('Selectable elements')
    class TestSelectablePage:
        @allure.description('Can select items in the List/Grid')
        @pytest.mark.parametrize('tab', ['list', 'grid'])
        def test_select_items(self, driver, tab):
            page = SelectablePage(driver, URL.SELECTABLE)
            page.open_page()

            items_to_select, active_items = page.select_items(tab)
            assert items_to_select == active_items, f'Items was not selected in the {tab}'

        @allure.description('Can deselect items in the List/Grid')
        @pytest.mark.parametrize('tab', ['list', 'grid'])
        def test_deselect_items(self, driver, tab):
            page = SelectablePage(driver, URL.SELECTABLE)
            page.open_page()

            page.select_items(tab)
            active_items_present = page.deselect_items(tab)
            assert active_items_present is False, f'Items was not deselected in the {tab}'

    @allure.feature('Resizable elements')
    class TestResizablePage:
        @allure.description('Can resize the Resizable box element, max and min sizes are correct')
        def test_resize_box(self, driver):
            page = ResizablePage(driver, URL.RESIZABLE)
            page.open_page()

            max_size, min_size = page.resize_box()
            assert max_size == (500, 300), 'Max size is not equal to 500x300'
            assert min_size == (150, 150), 'Min size is not equal to 150x150'

        @allure.description('Can resize the Resizable element')
        def test_resize_resizable(self, driver, check):
            page = ResizablePage(driver, URL.RESIZABLE)
            page.open_page()

            default_size, max_size, min_size = page.resize_resizable()
            with check:
                assert default_size[0] < max_size[0], 'The size was not increased along the X axis'
            with check:
                assert default_size[1] < max_size[1], 'The size was not increased along the Y axis'
            with check:
                assert min_size[0] < max_size[0], 'The size was not decreased along the X axis'
            with check:
                assert min_size[1] < max_size[1], 'The size was not decreased along the Y axis'
