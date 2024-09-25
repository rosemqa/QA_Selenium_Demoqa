import allure
from selenium import webdriver
import pytest
from datetime import datetime
from data.data import DOWNLOAD_DIR


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome, firefox or edge'
    )


@pytest.fixture(scope='class')
def driver(request):
    browser_name = request.config.getoption('--browser_name')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,  # директория для загрузки файлов
        "download.prompt_for_download": False,  # опц.
        "download.directory_upgrade": True,  # опц.
        "safebrowsing.enabled": True  # опц.
    })
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--headless=new')

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_preference("browser.download.folderList", 2)  # 2 для использования кастомного пути
    firefox_options.set_preference("browser.download.dir", DOWNLOAD_DIR)
    firefox_options.add_argument('--headless')

    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,  # директория для загрузки файлов
        "download.prompt_for_download": False,  # опц.
        "download.directory_upgrade": True,  # опц.
        "safebrowsing.enabled": True  # опц.
    })
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    # edge_options.add_argument("--start-maximized")
    edge_options.add_argument('--headless=new')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
        print('\nStart Chrome browser')
        # driver.maximize_window()
        driver.set_window_size(1920, 1080)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(options=firefox_options)
        print('\nStart Firefox browser')
        # driver.maximize_window()
        driver.set_window_size(1920, 1080)
    elif browser_name == 'edge':
        driver = webdriver.Edge(options=edge_options)
        # driver.maximize_window()
        driver.set_window_size(1920, 1080)
        print('\nStart Edge browser')
    else:
        raise pytest.UsageError('--browser_name should be chrome, firefox or edge')
    yield driver
    attachment = driver.get_screenshot_as_png()
    allure.attach(attachment, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
    print('\nQuit browser')
