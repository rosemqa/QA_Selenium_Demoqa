import time
import allure
import pytest
from data.links import URL
from pages.interactions_page import SortablePage


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
