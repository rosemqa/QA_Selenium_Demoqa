import random
import allure
from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators

    @allure.step('Get a list of sortable item values')
    def get_item_values_list(self, locators):
        items = self.find_elements(locators)
        return [i.text for i in items]

    @allure.step('Change the order of items in the List')
    def change_list_order(self):
        self.find_element(self.locators.LIST_TAB).click()
        order_before = self.get_item_values_list(self.locators.LIST_ITEM)
        two_random_items = random.sample(self.find_elements(self.locators.LIST_ITEM), k=2)
        what_item = two_random_items[0]
        where_item = two_random_items[1]
        self.drag_and_drop_to_element(what_item, where_item)
        order_after = self.get_item_values_list(self.locators.LIST_ITEM)
        return order_before, order_after

    @allure.step('Change the order of items in the Grid')
    def change_grid_order(self):
        self.find_element(self.locators.GRID_TAB).click()
        order_before = self.get_item_values_list(self.locators.GRID_ITEM)
        two_random_items = random.sample(self.find_elements(self.locators.GRID_ITEM), k=2)
        what_item = two_random_items[0]
        where_item = two_random_items[1]
        self.drag_and_drop_to_element(what_item, where_item)
        order_after = self.get_item_values_list(self.locators.GRID_ITEM)
        return order_before, order_after
