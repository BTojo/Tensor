import time
from selenium.webdriver.common.by import By

class Tensor:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tensor.ru/"

    def open_url(self):
        self.driver.get(self.url)

    def go_to_tensor(self):
        contacts_link = self.driver.find_element(By.CSS_SELECTOR,
                                                 'img[alt="Разработчик системы СБИС — компания «Тензор»"]')
        contacts_link.click()

    def power_is_in_people(self):
        power_is_in_people = self.driver.find_element(By.XPATH, "//p[text()='Сила в людях']")
        assert power_is_in_people.text == 'Сила в людях', "\nБлок сила в людях отсутствует"

    def go_to_about(self):
        about_link = self.driver.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", about_link)
        about_link.click()
        assert self.driver.current_url == 'https://tensor.ru/about', "URL не изменился"

    def verify_images_size(self):
        working_block = self.driver.find_element(By.XPATH,
                                                 "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']")
        # block_working = self.driver.find_element(By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']")
        time.sleep(5)
        images = working_block.find_elements(By.XPATH, ".//img")

        print("\nКоличество сравниваемых фотографий:" + str(len(images)))

        widths = []
        heights = []

        for image in images:
            width = image.size['width']
            height = image.size['height']
        widths.append(width)
        heights.append(height)

        assert len(set(widths)) == 1, "\nШирина фотографий не одинакова"
        assert len(set(heights)) == 1, "\nВысота фотографий не одинакова"