from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NeufsAutosElantra2018Page(BasePage):

    '''All locators for the neufs autos Elantra 2018 page should go here'''
    autos_elantra_2018_image = (By.CSS_SELECTOR, '.slide.active img[src*="cc_2018HYC020001_01_640_WAW.png"]')

    def check_neufs_elantra_2018_image_and_link(self):
        self.wait_autos_elantra_2018_image_to_display()
        assert self.browser.current_url == 'https://www.hyundailongueuil.com/neufs/Hyundai-Elantra-2018.html'

    def wait_autos_elantra_2018_image_to_display(self):
        self.wait.until(EC.visibility_of_element_located(self.autos_elantra_2018_image)).is_displayed()
