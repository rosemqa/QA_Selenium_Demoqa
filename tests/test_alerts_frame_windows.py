import time
import allure
import pytest
from data.links import URL
from pages.alert_frame_window_page import BrowserWindowPage, AlertsPage, FramesPage


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

    @allure.feature('Alerts')
    class TestAlerts:
        @allure.description('Can open an alert')
        def test_see_alert(self, driver):
            page = AlertsPage(driver, URL.ALERTS)
            page.open_page()

            alert_text = page.click_see_alert_button()
            assert alert_text == 'You clicked a button', 'Check alert text'

        @allure.description('Alert appears after 5 seconds')
        def test_delayed_alert(self, driver):
            page = AlertsPage(driver, URL.ALERTS)
            page.open_page()

            page.click_delayed_alert_button()
            assert page.is_not_alert_present(timeout=5), 'Alert should not be present for 5 sec, but it is'
            assert page.is_alert_present(timeout=0), 'Alert did not appear after 5 seconds'

            alert_text = page.get_alert_text()
            assert alert_text == 'This alert appeared after 5 seconds', 'Check alert text'

        @allure.description('Can accept or dismiss the alert')
        def test_confirm_alert(self, driver):
            page = AlertsPage(driver, URL.ALERTS)
            page.open_page()

            accept_result = page.check_confirm_alert('accept')
            dismiss_result = page.check_confirm_alert('dismiss')
            assert accept_result == 'You selected Ok', 'Check accept alert result text'
            assert dismiss_result == 'You selected Cancel', 'Check dismiss alert result text'

        @allure.description('Can open an alert with prompt')
        def test_prompt_alert(self, driver):
            page = AlertsPage(driver, URL.ALERTS)
            page.open_page()

            prompt_text, result_text = page.check_prompt_alert()
            assert f'You entered {prompt_text}' == result_text, 'Check result text'

    @allure.feature('Frames')
    class TestFrames:
        @allure.description('Check page with the frames')
        def test_frames(self, driver):
            page = FramesPage(driver, URL.FRAMES)
            page.open_page()

            first_frame = page.check_frame('first_frame')
            second_frame = page.check_frame('second_frame')

            assert first_frame == ('This is a sample page', '500px', '350px')
            assert second_frame == ('This is a sample page', '500px', '350px')


