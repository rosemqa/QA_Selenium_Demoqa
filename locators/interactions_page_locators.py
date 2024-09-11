from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, '#demo-tab-list')
    GRID_TAB = (By.CSS_SELECTOR, '#demo-tab-grid')
    LIST_ITEM = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item')
    GRID_ITEM = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item')


class SelectablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, '#demo-tab-list')
    GRID_TAB = (By.CSS_SELECTOR, '#demo-tab-grid')
    LIST_ITEM = (By.CSS_SELECTOR, '#demo-tabpane-list .list-group-item')
    ACTIVE_LIST_ITEM = (By.CSS_SELECTOR, '#demo-tabpane-list .active')
    GRID_ITEM = (By.CSS_SELECTOR, '#demo-tabpane-grid .list-group-item')
    ACTIVE_GRID_ITEM = (By.CSS_SELECTOR, '#demo-tabpane-grid .active')
