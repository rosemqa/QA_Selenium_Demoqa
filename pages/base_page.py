import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=10)

    def open_page(self):
        with allure.step(f'Open {self.url} page'):
            self.driver.get(self.url)

    def find_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator),
                               message=f"Can't find element by locator {locator}")

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}")

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    # def is_new_tab_open(self):
    #     self.wait.until(lambda d: len(d.window_handles) > 1, message='New browser tab/window was not open')

    @allure.step('Check that alert is present')
    def is_alert_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except TimeoutException:
            return False
        return True

    @allure.step('Check that alert is not present')
    def is_not_alert_present(self, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except TimeoutException:
            return True
        return False

    def switch_to_iframe(self, locator):
        return self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator),
                               message=f"Can't find iframe by locator {locator}")

    def get_current_url(self, timeout=1):
        time.sleep(timeout)
        return self.driver.current_url

    def sroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def move_to_element(self, locator):
        """Move cursor to element"""
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @allure.step('Double click')
    def double_click(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    @allure.step('Right click')
    def right_click(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    @allure.step('Drag and drop element to element')
    def drag_and_drop_to_element(self, what, where):
        what = self.find_element(what)
        where = self.find_element(where)
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where).perform()

    @allure.step('Drag and drop by offset')
    def drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords).perform()
