from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NeufsAutosAccent2017Page(BasePage):

    '''All locators for the neufs autos accent 2017 page should go here'''
    autos_accent_2017_image = (By.CSS_SELECTOR, '.slide.active img[src*="cc_2017HYC010002_01_640_PGU.png"]')

    def check_neufs_autos_accent_2017_image_and_link(self):
        assert self.browser.current_url == 'https://www.hyundailongueuil.com/neufs/Hyundai-Accent-2017.html'

    def wait_autos_accent_2017_image_to_display(self):
        self.wait.until(EC.visibility_of_element_located(self.autos_accent_2017_image)).is_displayed()
