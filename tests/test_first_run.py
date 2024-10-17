from pages.Sbis_page import SbisRuPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import time
from pages.Tensor_page import Tensor

logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG")


# @logger.catch()
def test_first(browser):
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
            (By.CSS_SELECTOR, 'img[alt="Разработчик системы СБИС — компания «Тензор»"]'))
    )

    sbis_ru_page.go_to_tensor()
    WebDriverWait(browser, 10).until(
        EC.url_changes("https://tensor.ru/")
    )
    tensor_ru_page = Tensor(browser)

    tensor_ru_page.open_url()
    time.sleep(10)

    tensor_ru_page.power_is_in_people()
    time.sleep(10)

    tensor_ru_page.go_to_about()
    time.sleep(10)
    tensor_ru_page.verify_images_size()
