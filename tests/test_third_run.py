from pages.Sbis_page import SbisRuPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG")


@logger.catch()
def test_third(browser):
    sbis_ru_page = SbisRuPage(browser)
    sbis_ru_page.open_url()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[text()='Скачать локальные версии']"))
    )

    sbis_ru_page.download_local_versions()
