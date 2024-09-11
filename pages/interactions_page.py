import random
import time
import allure
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators

    @allure.step('Get a list of sortable item values')
    def get_item_values_list(self, locators):
        items = self.find_elements(locators)
        return [i.text for i in items]

    @allure.step('Change the order of items in the List/Grid')
    def change_items_order(self, tab):
        tabs = {
            'list': {'tab': self.locators.LIST_TAB, 'item': self.locators.LIST_ITEM},
            'grid': {'tab': self.locators.GRID_TAB, 'item': self.locators.GRID_ITEM}
        }
        self.find_element(tabs[tab]['tab']).click()
        time.sleep(0.5)
        order_before = self.get_item_values_list(tabs[tab]['item'])
        two_random_items = random.sample(self.find_elements(tabs[tab]['item']), k=2)
        what_item = two_random_items[0]
        where_item = two_random_items[1]
        self.drag_and_drop_to_element(what_item, where_item)
        order_after = self.get_item_values_list(tabs[tab]['item'])
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators
    tabs = {
        'list': {'tab': locators.LIST_TAB,
                 'item': locators.LIST_ITEM,
                 'active_item': locators.ACTIVE_LIST_ITEM},
        'grid': {'tab': locators.GRID_TAB,
                 'item': locators.GRID_ITEM,
                 'active_item': locators.ACTIVE_GRID_ITEM}
    }

    @allure.step('Select the random items in the List/Grid')
    def select_items(self, tab):
        self.find_element(self.tabs[tab]['tab']).click()
        items = self.find_elements(self.tabs[tab]['item'])
        items_to_select = random.sample(items, k=random.randint(1, len(items)))
        for item in items_to_select:
            item.click()
        active_items = self.find_elements(self.tabs[tab]['active_item'])
        return len(items_to_select), len(active_items)

    @allure.step('Deselect items in the List/Grid')
    def deselect_items(self, tab):
        self.find_element(self.tabs[tab]['tab']).click()
        active_items = self.find_elements(self.tabs[tab]['active_item'])
        for item in active_items:
            item.click()
        return self.is_element_present(self.tabs[tab]['active_item'], timeout=1)
