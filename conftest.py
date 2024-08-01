import allure
from selenium import webdriver
import pytest
from data.data import DOWNLOAD_DIR


@pytest.fixture(scope='class')
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,  # директория для загрузки файлов
        "download.prompt_for_download": False,  # опц.
        "download.directory_upgrade": True,  # опц.
        "safebrowsing.enabled": True  # опц.
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    # attachment = driver.get_screenshot_as_png()
    # allure.attach(attachment, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
