from pages.Sbis_page import SbisRuPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import time


logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG")


@logger.catch()
def test_second(browser):
    sbis_ru_page = SbisRuPage(browser)
    sbis_ru_page.open_url()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                ".sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover"))
    )

    sbis_ru_page.go_to_contacts()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Костромская обл.']"))
    )
    sbis_ru_page.checking_region()
    time.sleep(1)
    sbis_ru_page.go_to_region()
