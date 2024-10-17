import time
from selenium.webdriver.common.by import By
import requests
import os

class SbisRuPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"


    def open_url(self):
        self.driver.get(self.url)

    def go_to_contacts(self):
        contacts1_link = self.driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover")
        contacts1_link.click()
        time.sleep(2)
        contacts2_link = self.driver.find_element(By.XPATH,"//span[text()='Еще 841 офис в России']")
        contacts2_link.click()

    def go_to_tensor(self):
        contacts_link = self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Разработчик системы СБИС — компания «Тензор»"]')
        contacts_link.click()


    def download_local_versions (self):
        local_versions = self.driver.find_element(By.XPATH, "//a[text()='Скачать локальные версии']")
        self.driver.execute_script("arguments[0].scrollIntoView();", local_versions)
        local_versions.click()
        time.sleep(5)

        object_to_download_link = self.driver.find_element(By.CSS_SELECTOR, 'a.sbis_ru-DownloadNew-loadLink__link.js-link[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
        object_text = object_to_download_link.text
        print('\n' + object_to_download_link.get_attribute("href"))
        print('\n' + object_text[12:18])
        time.sleep(5)

        download_url = object_to_download_link.get_attribute("href")
        download_directory = "D:\\git\\autotests\\downloads"
        response = requests.get(download_url)
        file_name = os.path.join(download_directory, "sbisplugin-setup-web.exe")

        with open(file_name, "wb") as file:
            file.write(response.content)
        if os.path.exists(file_name):
            print("Файл загрузился.")
        else:
            print("Файл не загрузился!")

        expected_file_size = 11.46
        file_size = os.path.getsize(file_name)
        print("Размер файла: " + str(round (file_size / (1024 * 1024), 2)) + " МБ")
        if abs((file_size / (1024 * 1024) / expected_file_size) - 1) < 0.005 :
            print("Размер файла соответствует указанному на сайте.")
        else:
            print("Размер файла не соответствует указанному на сайте.")

    def checking_region(self):
        self.url = self.driver.current_url
        region_element = self.driver.find_element(By.XPATH, "//span[text()='Костромская обл.']")
        partners_link = self.driver.find_element(By.CSS_SELECTOR,
                                                     ".sbisru-Contacts-List--ellipsis.pb-xm-12[itemprop='streetAddress']")

        assert region_element.text == 'Костромская обл.', "Регион не Костромская область"
        assert len(partners_link.text) > 0, "Партнеры отсутствуют"
        region_element.click()

    def go_to_region(self):
         new_region_element = self.driver.find_element(By.XPATH, "//span[text()='41 Камчатский край']")
         new_region_element.click()
         time.sleep(1)
         assert self.driver.find_element(By.XPATH,
                                            "//div[text()='Петропавловск-Камчатский']").text == 'Петропавловск-Камчатский', 'отсутствует "Петропавловск-Камчатский"'
         assert self.driver.title == 'СБИС Контакты — Камчатский край', 'Титул не "СБИС Контакты — Камчатский край"'
         assert self.driver.current_url != self.url, "URL не изменился"













