from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HyundaiCanadaHomePage(BasePage):

    '''All locators for the hyundai canada home page should go here'''
    region_selector_modal = (By.CSS_SELECTOR, '#regionSelectorModal > .modal-dialog')
    region_selector_title = (By.CSS_SELECTOR, 'h3#regionSelectorModal')

    def check_hyundai_canada_home_page_link(self):
        self.browser.switch_to_window(self.browser.window_handles[1])
        self.check_hyundai_canada_region_selector_modal()
        assert self.browser.current_url == 'https://www.hyundaicanada.com/fr'

    def check_hyundai_canada_region_selector_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.region_selector_modal)).is_displayed()
        assert self.browser.find_element(*self.region_selector_title).text == 'Il y a une Hyundai qui vous attend.'
