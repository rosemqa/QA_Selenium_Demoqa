import time
import allure
from data.links import URL
from pages.interactions_page import SortablePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable elements')
    class TestSortablePage:
        @allure.description('Can change the order of the List')
        def test_sort_list(self, driver):
            page = SortablePage(driver, URL.SORTABLE)
            page.open_page()

            order_before, order_after = page.change_list_order()
            assert order_before != order_after, 'The order of the List was not changed'

        @allure.description('Can change the order of the Gist')
        def test_sort_grid(self, driver):
            page = SortablePage(driver, URL.SORTABLE)
            page.open_page()

            order_before, order_after = page.change_grid_order()
            assert order_before != order_after, 'The order of the Grid was not changed'





