import random
import time
import allure
from selenium.webdriver import ActionChains

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
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


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    @allure.step('Get the size of the resizable element')
    def get_size(self, locator):
        size = self.find_element(locator).get_attribute('style')
        width = int(size.split(';')[0].split(': ')[1].rstrip('px'))
        height = int(size.split(';')[1].split(': ')[1].rstrip('px'))
        return width, height

    @allure.step('Resize the Resizable box element')
    def resize_box(self):
        handle = self.find_element(self.locators.RESIZABLE_BOX_HANDLE)
        self.drag_and_drop_by_offset(handle, 301, 101)
        max_size = self.get_size(self.locators.RESIZABLE_BOX)
        self.drag_and_drop_by_offset(handle, -360, -160)
        min_size = self.get_size(self.locators.RESIZABLE_BOX)
        return max_size, min_size

    @allure.step('Resize the Resizable element')
    def resize_resizable(self):
        default_size = self.get_size(self.locators.RESIZABLE)
        handle = self.find_visible_element(self.locators.RESIZABLE_HANDLE)
        self.drag_and_drop_by_offset(handle, 500, 50)
        max_size = self.get_size(self.locators.RESIZABLE)
        self.drag_and_drop_by_offset(handle, -150, -150)
        min_size = self.get_size(self.locators.RESIZABLE)
        return default_size, max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators

    @allure.step('Drop the Drag element into the Drop element on the Simple tab')
    def drop_simple(self):
        self.find_element(self.locators.SIMPLE_TAB).click()
        drag = self.locators.SIMPLE_DRAG_ME
        drop = self.locators.SIMPLE_DROP_HERE
        self.drag_and_drop_to_element(drag, drop)
        drop_text = self.find_element(drop).text
        return drop_text

    @allure.step('Drop the Not Acceptable and Acceptable elements into the Drop element on the Accept tab')
    def drop_acceptable(self):
        self.find_element(self.locators.ACCEPT_TAB).click()
        acceptable_drag = self.locators.ACCEPTABLE
        not_acceptable_drag = self.locators.NOT_ACCEPTABLE
        drop = self.locators.ACCEPT_DROP_HERE
        self.drag_and_drop_to_element(not_acceptable_drag, drop)
        not_acceptable_drop_text = self.find_element(drop).text
        self.drag_and_drop_to_element(acceptable_drag, drop)
        acceptable_drop_text = self.find_element(drop).text
        return not_acceptable_drop_text, acceptable_drop_text

    @allure.step('Drop the Drag element into Not greedy inner box and Greedy inner box on the Prevent propagation tab')
    def drop_prevent_propagation(self):
        self.find_element(self.locators.PREVENT_TAB).click()

        drag = self.find_element(self.locators.PREVENT_DRAG_ME)
        not_greedy_inner_drop = self.find_element(self.locators.NOT_GREEDY_INNER_DROP_BOX)
        greedy_inner_drop = self.find_element(self.locators.GREEDY_INNER_DROP_BOX)

        self.drag_and_drop_to_element(drag, not_greedy_inner_drop)
        not_greedy_outer_text = self.find_element(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        not_greedy_inner_text = not_greedy_inner_drop.text

        self.drag_and_drop_to_element(drag, greedy_inner_drop)
        greedy_outer_text = self.find_element(self.locators.GREEDY_DROP_BOX_TEXT).text
        greedy_inner_text = greedy_inner_drop.text

        return not_greedy_outer_text, not_greedy_inner_text, greedy_outer_text, greedy_inner_text

    @allure.step('Drop the Will Revert and the Not Revert elements into the Drop element on the revert draggable tab')
    def drop_revert_draggable(self, drag_type):
        drags = {
            'will revert': self.locators.WILL_REVERT,
            'not revert': self.locators.NOT_REVERT
        }
        self.find_element(self.locators.REVERT_TAB).click()

        drag = self.find_element(drags[drag_type])
        drop = self.find_element(self.locators.REVERT_DROP_HERE)

        self.drag_and_drop_to_element(drag, drop)
        drag_position_after_drop = drag.get_attribute('style')
        time.sleep(1)
        drag_final_position = drag.get_attribute('style')

        return drag_position_after_drop, drag_final_position


class DraggablePage(BasePage):
    locators = DraggablePageLocators

    @allure.step('Get the X and Y coordinates of the drag element')
    def get_drag_position(self, element):
        position = element.get_attribute('style')
        if position != 'position: relative;':
            x = int(position.split(';')[1].split(': ')[1].rstrip('px'))  # или int(re.findall(r'-?\d+', position)[0])
            y = int(position.split(';')[2].split(': ')[1].rstrip('px'))  # или int(re.findall(r'-?\d+', position)[1])
            return x, y
        return None, None

    @allure.step('Drag the element on the Simple tab')
    def drag_simple(self):
        self.find_element(self.locators.SIMPLE_TAB).click()
        drag = self.find_element(self.locators.SIMPLE_DRAG_ME)
        expected_x = random.randint(-100, 500)
        expected_y = random.randint(-100, 500)
        self.drag_and_drop_by_offset(drag, expected_x, expected_y)
        actual_x, actual_y = self.get_drag_position(drag)
        return actual_x, actual_y, expected_x, expected_y

    @allure.step('Drag the Only X element on the Axis Restricted tab')
    def drag_only_x(self):
        self.find_element(self.locators.AXIS_TAB).click()
        drag = self.find_element(self.locators.ONLY_X)
        expected_x = random.randint(-100, 500)
        self.drag_and_drop_by_offset(drag, expected_x, random.randint(-100, 500))
        actual_x, actual_y = self.get_drag_position(drag)
        return actual_x, actual_y, expected_x

    @allure.step('Drag the Only Y element on the Axis Restricted tab')
    def drag_only_y(self):
        self.find_element(self.locators.AXIS_TAB).click()
        drag = self.find_element(self.locators.ONLY_Y)
        expected_y = random.randint(-100, 500)
        self.drag_and_drop_by_offset(drag, random.randint(-100, 500), expected_y)
        actual_x, actual_y = self.get_drag_position(drag)
        return actual_x, actual_y, expected_y

    @allure.step('Drag the elements on the Cursor Style tab')
    def drag_cursor_style_elements(self, cursor_location):
        cursor = {
            'center': self.locators.CENTER,
            'top_left': self.locators.TOP_LEFT,
            'bottom': self.locators.BOTTOM
        }
        self.find_element(self.locators.STYLE_TAB).click()
        element = self.find_element(cursor[cursor_location])
        x_offset = random.randint(1, 500)
        y_offset = random.randint(1, 100)
        # Определяем начальные координаты верхнего левого угла элемента
        initial_element_location = element.location
        initial_top_left_x = initial_element_location['x']
        initial_top_left_y = initial_element_location['y']

        # Получаем размеры элемента (ширину и высоту)
        element_size = element.size
        element_width = element_size['width']
        element_height = element_size['height']

        # проверяем стиль курсора элемента
        cursor_style = (self.driver.execute_script("return window.getComputedStyle(arguments[0]).cursor;", element))
        # или cursor_style = element.value_of_css_property('cursor')

        action = ActionChains(self.driver)
        action.click_and_hold(element).perform()
        action.move_by_offset(x_offset, y_offset).perform()

        # Проверяем стиль курсора во время перетаскивания
        cursor_style_during_drag = self.driver.execute_script("return window.getComputedStyle(document.body).cursor;")

        # Определяем ожидаемые координаты верхнего левого угла элемента при перетаскивании
        if cursor_location == 'center':
            offset_correction = -6  # Коррекция смещения в зависимости от перемещения
            expected_top_left_x = initial_top_left_x + x_offset + offset_correction
            expected_top_left_y = initial_top_left_y + y_offset + offset_correction
        elif cursor_location == 'top_left':
            offset_correction = 5  # Коррекция смещения в зависимости от перемещения
            expected_top_left_x = initial_top_left_x + element_width // 2 + x_offset + offset_correction
            expected_top_left_y = initial_top_left_y + element_height // 2 + y_offset + offset_correction
        elif cursor_location == 'bottom':
            expected_top_left_x = initial_top_left_x + x_offset
            expected_top_left_y = initial_top_left_y - element_height // 2 + y_offset

        # Определяем текущие координаты верхнего левого угла элемента
        element_location = element.location
        top_left_x = element_location['x']
        top_left_y = element_location['y']

        return cursor_style, cursor_style_during_drag, expected_top_left_x, expected_top_left_y, top_left_x, top_left_y
