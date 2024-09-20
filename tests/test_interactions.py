import allure
import pytest
from data.links import URL
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


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

    @allure.feature('Droppable elements')
    class TestDroppablePage:
        @allure.description('Can drop the drag element into the drop element')
        def test_simple_drop(self, driver):
            page = DroppablePage(driver, URL.DROPPABLE)
            page.open_page()

            drop_text = page.drop_simple()
            assert drop_text == 'Dropped!', 'The Drag element was not dropped'

        @allure.description('Drop element can accept or reject relevant drag elements')
        def test_acceptable_drop(self, driver):
            page = DroppablePage(driver, URL.DROPPABLE)
            page.open_page()

            not_acceptable_drop, acceptable_drop = page.drop_acceptable()
            assert not_acceptable_drop == 'Drop here', 'The Not Acceptable Drag element was accepted'
            assert acceptable_drop == 'Dropped!', 'The Acceptable Drag element was not accepted'

        @allure.description('Check the different reactions of Drop elements when dragging a Drag element into them')
        def test_prevent_propagation_drop(self, driver, check):
            page = DroppablePage(driver, URL.DROPPABLE)
            page.open_page()

            (not_greedy_outer_text,
             not_greedy_inner_text,
             greedy_outer_text,
             greedy_inner_text) = page.drop_prevent_propagation()
            with check:
                assert not_greedy_outer_text == 'Dropped!', 'The text was not changed in the not greedy outer box'
            with check:
                assert not_greedy_inner_text == 'Dropped!', 'The text was not changed in the not greedy inner box'
            with check:
                assert greedy_outer_text == 'Outer droppable', 'The text was changed in the greedy outer box'
            with check:
                assert greedy_inner_text == 'Dropped!', 'The text was not changed in the greedy inner box'

        @allure.description('Drop element can revert or not revert relevant drag elements')
        def test_drop_revert_draggable(self, driver, check):
            page = DroppablePage(driver, URL.DROPPABLE)
            page.open_page()

            will_drag_position_after_drop, will_drag_final_position = page.drop_revert_draggable('will revert')
            not_drag_position_after_drop, not_drag_final_position = page.drop_revert_draggable('not revert')
            with (check):
                assert will_drag_position_after_drop != will_drag_final_position, \
                    'The Will Revert element was not reverted'
            with (check):
                assert not_drag_position_after_drop == not_drag_final_position, \
                    'The Not Revert element was reverted'

    @allure.feature('Draggable elements')
    class TestDraggablePage:
        @allure.description('Can drag the element along X and Y axes')
        def test_simple_drag(self, driver, check):
            page = DraggablePage(driver, URL.DRAGGABLE)
            page.open_page()

            actual_x, actual_y, expected_x, expected_y = page.drag_simple()
            with check:
                assert actual_x == expected_x, 'Drag element was not moved along the X axis the expected distance'
            with check:
                assert actual_y == expected_y, 'Drag element was not moved along the Y axis the expected distance'

        @allure.description('Can drag the element only along X axis')
        def test_x_axis_restricted_drag(self, driver, check):
            page = DraggablePage(driver, URL.DRAGGABLE)
            page.open_page()

            actual_x, actual_y, expected_x = page.drag_only_x()
            with check:
                assert actual_y == 0, 'Drag element was moved along the Y axis'
            with check:
                assert actual_x == expected_x, 'Drag element was not moved along the X axis the expected distance'

        @allure.description('Can drag the element only along Y axis')
        def test_y_axis_restricted_drag(self, driver, check):
            page = DraggablePage(driver, URL.DRAGGABLE)
            page.open_page()

            actual_x, actual_y, expected_y = page.drag_only_y()
            with check:
                assert actual_x == 0, 'Drag element was moved along the X axis'
            with check:
                assert actual_y == expected_y, 'Drag element was not moved along the Y axis the expected distance'

        @allure.description('The draggable element can not be drugged outside the container')
        def test_container_restricted_drag(self, driver):
            page = DraggablePage(driver, URL.DRAGGABLE)
            page.open_page()

            (drag_box_bottom_right_x,
             drag_box_bottom_right_y,
             container_bottom_right_x,
             container_bottom_right_y) = page.drag_element_inside_container()

            assert (drag_box_bottom_right_x < container_bottom_right_x and
                    drag_box_bottom_right_y < container_bottom_right_y), \
                'The draggable element was drugged outside the container'

        @allure.description('Check the cursor style and cursor location while dragging')
        @pytest.mark.parametrize('cursor_location, style', [('center', 'move'),
                                                            ('top_left', 'crosshair'),
                                                            ('bottom', 'auto')])
        def test_cursor_style(self, driver, check, cursor_location, style):
            page = DraggablePage(driver, URL.DRAGGABLE)
            page.open_page()

            (cursor_style,
             cursor_style_during_drag,
             expected_top_left_x,
             expected_top_left_y,
             top_left_x,
             top_left_y) = page.drag_cursor_style_elements(cursor_location)
            with check:
                assert cursor_style == 'move', f'Expected "move" initial cursor style, but got "{cursor_style}"'
            with check:
                assert cursor_style_during_drag == style, \
                    f'Expected "{style}" cursor style, but got "{cursor_style_during_drag}" while dragging'
            with check:
                assert top_left_x == expected_top_left_x and top_left_y == expected_top_left_y, \
                    f'Cursor is not in the {cursor_location} of the element when dragging'
