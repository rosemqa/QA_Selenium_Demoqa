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


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, '#resizableBoxWithRestriction')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, '#resizableBoxWithRestriction .react-resizable-handle')
    RESIZABLE = (By.CSS_SELECTOR, '#resizable')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, '#resizable .react-resizable-handle')


class DroppablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, '#draggable')
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    ACCEPT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, '#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, '#notAcceptable')
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    PREVENT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-preventPropogation')
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, '#dragBox')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, '#notGreedyDropBox>p')
    NOT_GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, '#notGreedyInnerDropBox')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, '#greedyDropBox>p')
    GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, '#greedyDropBoxInner')

    REVERT_TAB = (By.CSS_SELECTOR, '#droppableExample-tab-revertable')
    WILL_REVERT = (By.CSS_SELECTOR, '#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, '#notRevertable')
    REVERT_DROP_HERE = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, '#dragBox')

    AXIS_TAB = (By.CSS_SELECTOR, '#draggableExample-tab-axisRestriction')
    ONLY_X = (By.CSS_SELECTOR, '#restrictedX')
    ONLY_Y = (By.CSS_SELECTOR, '#restrictedY')
