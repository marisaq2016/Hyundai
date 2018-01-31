import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pageobjects.home_page import HomePage
from pageobjects.hyundai_canada_home_page import HyundaiCanadaHomePage
from pageobjects.neufs_autos_accent_2017_page import NeufsAutosAccent2017Page
from pageobjects.neufs_autos_elantra_2018_page import NeufsAutosElantra2018Page
from pageobjects.neufs_page import NeufsPage


class Base:

    '''All locators for the base should go here'''
    main_div = (By.CSS_SELECTOR, '#mainDiv > .top_bg tr[valign="top"]')
    hyundai_longueuil_body = (By.CSS_SELECTOR, 'body.FRENCH')
    image_slider = (By.CSS_SELECTOR, '#homepage-banner > .slider-wrapper.theme-default > div > #slider')
    hyundai_longueuil_toast_close = (By.CSS_SELECTOR, '#toast-container > div > button')
    hyundai_longueuil_toast_title = (By.CSS_SELECTOR, '#toast-container > div > div.toast-titles')
    hyundai_longueuil_toast_message = (By.CSS_SELECTOR, '#toast-container > div > div.toast-messages')
    promo_banner = (By.CSS_SELECTOR, '#defaultTopBanner #defaultTopBannerWrap')
    promo_banner_title = (By.CSS_SELECTOR, '#defaultTopBannerTitle')
    promo_banner_text = (By.CSS_SELECTOR, '#defaultTopBannerText')
    promo_banner_button = (By.CSS_SELECTOR, '#defaultTopBannerBtn')
    make_model_year = (By.CSS_SELECTOR, '.makeModelYear')
    car_price = (By.CSS_SELECTOR, '#carPrice')
    car_price_discount = (By.CSS_SELECTOR, '#carPriceDisc')
    car_price_promo = (By.CSS_SELECTOR, '#carPricePromo')

    @pytest.fixture()
    def _init_pages(self):
        self.home_page = HomePage(self.browser, self.wait, self.hover)
        self.neufs_page = NeufsPage(self.browser, self.wait, self.hover)
        self.hyundai_canada_home_page = HyundaiCanadaHomePage(self.browser, self.wait, self.hover)
        self.neufs_autos_accent_2017_page = NeufsAutosAccent2017Page(self.browser, self.wait, self.hover)
        self.neufs_autos_elantra_2018_page = NeufsAutosElantra2018Page(self.browser, self.wait, self.hover)

    @pytest.fixture(autouse=True)
    @pytest.mark.usefixtures("_init_pages")
    def setup_and_teardown_browser(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 90)
        self.hover = ActionChains(self.browser)
        self.browser.maximize_window()
        self.open_hyundai_longueuil_url_and_wait_home_page_to_load()
        yield
        self.browser.close()
        self.browser.quit()

    def open_hyundai_longueuil_url_and_wait_home_page_to_load(self):
        self.browser.get('https://www.hyundailongueuil.com/')
        self.wait_for_home_page_to_be_loaded()
        self.check_and_close_toast_message()

    def wait_for_home_page_to_be_loaded(self):
        self.wait.until(EC.title_is, 'Concessionnaire Hyundai Longueuil \
            (près de Brossard, Ste-Julie et Montréal) | Hyundai à vendre \
            à Longueuil (près de Brossard, Ste-Julie et Montréal)')
        self.browser.find_element(*self.hyundai_longueuil_body)
        self.browser.find_element(*self.image_slider).is_displayed()
        self.wait_the_main_div_to_display()

    def wait_the_main_div_to_display(self):
        self.wait.until(EC.element_to_be_clickable(self.main_div)).is_displayed()

    def check_and_close_toast_message(self):
        toast_message = self.wait.until(EC.invisibility_of_element_located(self.hyundai_longueuil_toast_message))
        if not toast_message:
            assert self.browser.find_element(*self.hyundai_longueuil_toast_title).text == \
                'NOUVEAU: CONFIGURATEUR HYUNDAI!'
            assert self.browser.find_element(*self.hyundai_longueuil_toast_message).text == \
                'Construisez votre véhicule et découvrez nos meilleurs prix! Cliquez pour débuter!'
            self.browser.find_element(*self.hyundai_longueuil_toast_close).click()
        self.wait.until(EC.invisibility_of_element_located(self.hyundai_longueuil_toast_close))

    def wait_and_check_promo_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.promo_banner))
        assert self.browser.find_element(*self.promo_banner_title).text == 'Entrez voir nos PROMOTIONS!'
        assert self.browser.find_element(*self.promo_banner_text).text == 'Vous serez surpris!'
        assert self.browser.find_element(*self.promo_banner_button).text == 'CLIQUEZ ICI'

    def check_make_model_year(self, expected_make_model_year):
        assert self.browser.find_element(*self.make_model_year).text == expected_make_model_year

    def check_the_car_price(self, expected_car_price):
        assert self.browser.find_element(*self.car_price).text == expected_car_price

    def check_the_car_price_discount(self, expected_discount):
        assert self.browser.find_element(*self.car_price_discount).text == expected_discount

    def check_the_car_price_promo(self, expected_car_price_promo):
        assert self.browser.find_element(*self.car_price_promo).text == expected_car_price_promo
