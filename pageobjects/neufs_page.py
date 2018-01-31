from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NeufsPage(BasePage):

    '''All locators for the neufs page should go here'''
    autos_neuves = (By.CSS_SELECTOR, '#classcar_container .car_box.car_box22')
    vus_neufs = (By.CSS_SELECTOR, '#classsuv_container .car_box.car_box22')
    hybrides_neuves = (By.CSS_SELECTOR, '#classhybrid_container .car_box.car_box22')
    electrique_neuves = (By.CSS_SELECTOR, '#classelectric_container .car_box.car_box22')

    def check_neufs_link(self):
        self.wait_the_different_category_of_neufs_cars_to_display()
        self.check_neufs_title()
        assert self.browser.current_url == 'https://www.hyundailongueuil.com/neufs/Hyundai.html'

    def check_neufs_title(self):
        assert self.wait.until(EC.title_is, 'Hyundai 2018 & 2019 à Longueuil, Brossard & Montreal.')

    def wait_the_different_category_of_neufs_cars_to_display(self):
        self.wait.until(EC.element_to_be_clickable(self.autos_neuves)).is_displayed()
        self.wait.until(EC.element_to_be_clickable(self.vus_neufs)).is_displayed()
        self.wait.until(EC.element_to_be_clickable(self.hybrides_neuves)).is_displayed()
        self.wait.until(EC.element_to_be_clickable(self.electrique_neuves)).is_displayed()
