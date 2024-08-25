import time
import allure
import pytest
from data.links import URL
from pages.alert_frame_window_page import BrowserWindowPage


class TestAlertsFrameWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        @allure.description('Can open a new browser tab/window')
        @pytest.mark.parametrize('button_name', ['tab', 'window'])
        def test_new_browser_window(self, driver, button_name):
            page = BrowserWindowPage(driver, URL.BROWSER_WINDOWS)
            page.open_page()

            new_window = page.open_new_tab_or_window(button_name)
            assert new_window is True, f'The new {button_name} was not open'

            window_text = page.get_title_text_on_the_new_window()
            assert window_text == 'This is a sample page', f'Check title text on the new browser {button_name}'
