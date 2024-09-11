import time
import allure
import pytest
from data.links import URL
from pages.interactions_page import SortablePage, SelectablePage


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
