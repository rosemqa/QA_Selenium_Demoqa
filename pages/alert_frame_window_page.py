import time
from datetime import datetime
import allure
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesLocators, ModalDialogsPageLocators
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


class AlertsPage(BasePage):
    locators = AlertsPageLocators

    @allure.step('Switch to alert and get its text')
    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    @allure.step('Click see alert button')
    def click_see_alert_button(self):
        self.find_element(self.locators.SEE_ALERT_BTN).click()
        return self.get_alert_text()

    @allure.step('Click delayed alert button')
    def click_delayed_alert_button(self):
        self.driver.refresh()
        self.find_element(self.locators.ALERT_AFTER_5_SECONDS_BTN).click()

    @allure.step('Click confirm alert button, accept or dismiss alert and get result text')
    def check_confirm_alert(self, action):
        self.find_element(self.locators.CONFIRM_BOX_ALERT_BTN).click()
        alert = self.driver.switch_to.alert
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        result = self.find_element(self.locators.CONFIRM_RESULT).text
        return result

    @allure.step('Click prompt alert button, enter text in alert, accept and get result text')
    def check_prompt_alert(self):
        input_text = str(datetime.now())
        self.find_element(self.locators.PROMPT_BOX_ALERT_BTN).click()
        prompt = self.driver.switch_to.alert
        prompt.send_keys(input_text)
        prompt.accept()
        result_text = self.find_element(self.locators.PROMPT_RESULT).text
        return input_text, result_text


class FramesPage(BasePage):
    locators = FramesPageLocators

    @allure.step('Get iframes properties, switch to iframes, get text in the iframes')
    def check_iframes(self, frame_number):
        if frame_number == 'first_frame':
            frame = self.find_element(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            frame_text = self.find_element(self.locators.FRAME_TITLE).text
            self.driver.switch_to.default_content()  # return to the content of the page from a frame
            return frame_text, width, height
        elif frame_number == 'second_frame':
            frame = self.find_element(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            frame_text = self.find_element(self.locators.FRAME_TITLE).text
            return frame_text, width, height


class NestedFramesPage(BasePage):
    locators = NestedFramesLocators

    @allure.step('Switch to iframes and get text in the iframes')
    def check_nested_frames(self):
        self.switch_to_iframe(self.locators.PARENT_FRAME)
        parent_text = self.find_element(self.locators.FRAME_TEXT).text

        self.switch_to_iframe(self.locators.CHILD_FRAME)
        child_text = self.find_element(self.locators.FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    def get_modal_text(self):
        return self.find_element(self.locators.MODAL_TEXT).text

    @allure.step('Open small/large model, get title text and body text length')
    def check_modal(self):
        self.find_element(self.locators.SMALL_MODAL_BTN).click()
        small_modal_text = self.get_modal_text()
        small_title_text = self.find_element(self.locators.SMALL_MODAL_TITLE).text
        self.find_element(self.locators.CLOSE_SMALL_MODAL_BTN).click()

        self.find_element(self.locators.LARGE_MODAL_BTN).click()
        large_modal_text = self.get_modal_text()
        large_title_text = self.find_element(self.locators.LARGE_MODAL_TITLE).text
        return [small_title_text, len(small_modal_text)], [large_title_text, len(large_modal_text)]
