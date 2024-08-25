import time
import allure
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowsPageLocators

    @allure.step('Get title text on the new browser tab/window')
    def get_title_text_on_the_new_window(self):
        text = self.find_element(self.locators.NEW_TAB_TITLE_TEXT).text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return text

    @allure.step('Open a new browser tab/window ')
    def open_new_tab_or_window(self, button):
        buttons = {
            'tab': self.locators.NEW_TAB_BTN,
            'window': self.locators.NEW_WINDOW_BTN
        }
        self.find_element(buttons[button]).click()
        windows = self.driver.window_handles
        if len(windows) == 2:
            new_window = self.driver.window_handles[1]
            self.driver.switch_to.window(new_window)
            return True
        return False
