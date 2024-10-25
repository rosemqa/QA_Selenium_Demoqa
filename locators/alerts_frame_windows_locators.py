from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, '#tabButton')
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE_BTN = (By.CSS_SELECTOR, '#messageWindowButton')
    NEW_TAB_TITLE_TEXT = (By.CSS_SELECTOR, '#sampleHeading')


class AlertsPageLocators:
    SEE_ALERT_BTN = (By.CSS_SELECTOR, '#alertButton')
    ALERT_AFTER_5_SECONDS_BTN = (By.CSS_SELECTOR, '#timerAlertButton')
    CONFIRM_BOX_ALERT_BTN = (By.CSS_SELECTOR, '#confirmButton')
    PROMPT_BOX_ALERT_BTN = (By.CSS_SELECTOR, '#promtButton')
    CONFIRM_RESULT = (By.CSS_SELECTOR, '#confirmResult')
    PROMPT_RESULT = (By.CSS_SELECTOR, '#promptResult')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, '#frame1')
    SECOND_FRAME = (By.CSS_SELECTOR, '#frame1')
    FRAME_TITLE = (By.CSS_SELECTOR, '#sampleHeading')


class NestedFramesLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, '#frame1')
    CHILD_FRAME = (By.CSS_SELECTOR, '[srcdoc="<p>Child Iframe</p>"]')
    FRAME_TEXT = (By.CSS_SELECTOR, 'body')


class ModalDialogsPageLocators:
    SMALL_MODAL_BTN = (By.CSS_SELECTOR, '#showSmallModal')
    CLOSE_SMALL_MODAL_BTN = (By.CSS_SELECTOR, '#closeSmallModal')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, '#example-modal-sizes-title-sm')

    LARGE_MODAL_BTN = (By.CSS_SELECTOR, '#showLargeModal')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, '#example-modal-sizes-title-lg')

    MODAL_TEXT = (By.CSS_SELECTOR, '.modal-body')
    MODAL_OVERLAY = (By.CSS_SELECTOR, '.modal')
