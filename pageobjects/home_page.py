from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    '''All locators for the home page should go here'''
    alert_message = (By.CSS_SELECTOR, '#alertMsgContent')
    hyundai_longueuil_logo = (By.CSS_SELECTOR, '.logo')
    home_icon_link = (By.CSS_SELECTOR, '#MainMenu_HOME > a')
    neufs_link = (By.CSS_SELECTOR, '#MainMenu_NEW > a')
    neufs_menu = (By.CSS_SELECTOR, '#MainMenu_NEW')
    neufs_autos_menu = (By.CSS_SELECTOR, '#MainMenu_NEW_SEDAN')
    neufs_autos_accent_2017_menu = (By.CSS_SELECTOR, '.sub li.firstItem.hasImg \
        > a[href*="Hyundai-Accent-2017.html"]:nth-child(3)')
    neufs_autos_accent_hatchback_2017_menu = (By.CSS_SELECTOR, '.sub li.hasImg \
        > a[href*="Hyundai-Accent Hatchback-2017.html"]:nth-child(3)')
    neufs_autos_elantra_2018_menu = (By.CSS_SELECTOR, '.sub li.hasImg > \
        a[href*="Hyundai-Elantra-2018.html"]:nth-child(3)')
    promotions_side_button = (By.CSS_SELECTOR, 'div#promotionSideVButton > a.promotionSideBtnA')
    promotions_side_button_popup = (By.CSS_SELECTOR, '#scratchAndSavePopupContainer_other')
    promotion_popup_title = (By.CSS_SELECTOR, 'div[class*="scratchbody"] > .scratchbody2_title')
    promotion_popup_below_the_title = (By.CSS_SELECTOR, '.scratchTitle')
    promotion_popup_button = (By.CSS_SELECTOR, '.scratchbtn.buttonTwo.bg_default')
    nom_field = (By.CSS_SELECTOR, '#rebateName_other')
    courriel_field = (By.CSS_SELECTOR, '#rebateEmail_other')
    telephone_field = (By.CSS_SELECTOR, '#rebatePhone_other')
    vehicule_recherche = (By.CSS_SELECTOR, '#rebateSearchedVehicle_other')
    canvas = (By.CSS_SELECTOR, '.scratchDivText > canvas')
    textarea_message = (By.CSS_SELECTOR, '.textarea')
    imprimez_button = (By.CSS_SELECTOR, 'input[style*="display:block"]#printBtnOverlay_other')
    textez_nous_side_button = (By.CSS_SELECTOR, '#slideit > label.open')
    textez_nous_title = (By.CSS_SELECTOR, 'section > span.title')
    textez_nous_nous_info = (By.CSS_SELECTOR, '.wrap > p.info')
    textez_nous_nom_field = (By.CSS_SELECTOR, '.jqTransformInputInner > div > input#nameSlide')
    textez_nous_mobile_field = (By.CSS_SELECTOR, '#SlideWidgetForm > div > div:nth-child(4) > div')
    textez_nous_departement_dropdown = (By.CSS_SELECTOR, '#SlideWidgetForm > \
        div > div:nth-child(6) > div > div > span')
    textez_nous_message_area = (By.CSS_SELECTOR, '#jqTransformTextarea-mm > div > textarea#query_area')
    textez_nous_soumettre_button = (By.CSS_SELECTOR, 'a[onclick="slideForm.submitSlideForm()"]')
    first_slide_image = (By.CSS_SELECTOR, '#slider > img[src*="Hyundai_Longueuil_JAN_banner_960x300_01.jpg"]')
    second_slide_image = (By.CSS_SELECTOR, '#slider > img[src*="Hyundai_Longueuil_JAN_banner_960x300_04.jpg"]')
    third_slide_image = (By.CSS_SELECTOR, '#slider > img[src*="Hyundai_Longueuil_JAN_banner_960x300_03.jpg"]')
    fourth_slide_image = (By.CSS_SELECTOR, '#slider > img[src*="Hyundai_Longueuil_JAN_banner_960x300_02.jpg"]')
    fifth_slide_image = (By.CSS_SELECTOR, '#slider > img[src*="Hyundai_Longueuil_banner_OCT_960x300_06.jpg"]')

    def click_hyundai_longueuil_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.hyundai_longueuil_logo)).click()

    def click_home_icon_link(self):
        self.wait.until(EC.element_to_be_clickable(self.home_icon_link)).click()

    def click_neufs_link(self):
        self.wait.until(EC.element_to_be_clickable(self.neufs_link)).click()

    def click_neufs_autos_accent_2017_menu(self):
        neufs_menu = self.browser.find_element(*self.neufs_menu)
        neufs_autos_menu = self.browser.find_element(*self.neufs_autos_menu)
        neufs_autos_accent_2017_menu = self.browser.find_element(*self.neufs_autos_accent_2017_menu)
        self.hover.move_to_element(neufs_menu).move_to_element(neufs_autos_menu) \
            .move_to_element(neufs_autos_accent_2017_menu).click().perform()

    def click_neufs_autos_accent_hatchback_2017_menu(self):
        neufs_menu = self.browser.find_element(*self.neufs_menu)
        neufs_autos_menu = self.browser.find_element(*self.neufs_autos_menu)
        neufs_autos_accent_hatchback_2017_menu = self.browser.find_element(*self.neufs_autos_accent_hatchback_2017_menu)
        self.hover.move_to_element(neufs_menu).move_to_element(neufs_autos_menu) \
            .move_to_element(neufs_autos_accent_hatchback_2017_menu).click().perform()

    def click_neufs_autos_elantra_2018_menu(self):
        neufs_menu = self.browser.find_element(*self.neufs_menu)
        neufs_autos_menu = self.browser.find_element(*self.neufs_autos_menu)
        neufs_autos_elantra_2018_menu = self.browser.find_element(*self.neufs_autos_elantra_2018_menu)
        self.hover.move_to_element(neufs_menu).move_to_element(neufs_autos_menu) \
            .move_to_element(neufs_autos_elantra_2018_menu).click().perform()

    def click_promotions_side_button(self):
        self.wait.until(EC.element_to_be_clickable(self.promotions_side_button)).click()

    def check_the_promotions_side_button_popup(self):
        self.wait_promotions_popup_to_display()
        self.check_the_promotions_popup_text()
        self.check_the_promotions_popup_fields_to_be_clickable()
        self.wait.until(EC.visibility_of_element_located(self.canvas))
        assert self.browser.find_element(*self.imprimez_button)

    def click_textez_nous_side_button(self):
        self.wait.until(EC.element_to_be_clickable(self.textez_nous_side_button)).click()

    def check_textez_nous_popup(self):
        assert self.wait.until(EC.visibility_of_element_located(self.textez_nous_title)).text == 'TEXTEZ-NOUS!'
        assert self.browser.find_element(*self.textez_nous_nous_info).text == \
            'Recevez nos promotions par texto ou réponses à vos questions!'
        self.wait.until(EC.element_to_be_clickable(self.textez_nous_nom_field))
        self.wait.until(EC.element_to_be_clickable(self.textez_nous_mobile_field))
        self.wait.until(EC.element_to_be_clickable(self.textez_nous_departement_dropdown))
        self.wait.until(EC.element_to_be_clickable(self.textez_nous_message_area))
        self.wait.until(EC.element_to_be_clickable(self.textez_nous_soumettre_button))

    def click_slide_image_from_home_page(self, nth_expected_image):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#homepage-banner \
            > div > div > div.nivo-controlNav > a:nth-child({})'.format(nth_expected_image)))).click()

    def check_that_the_first_image_displayed(self):
        assert self.wait.until(EC.element_to_be_clickable(self.first_slide_image)).is_displayed()

    def check_that_the_second_image_displayed(self):
        assert self.wait.until(EC.element_to_be_clickable(self.second_slide_image)).is_displayed()

    def check_that_the_third_image_displayed(self):
        assert self.wait.until(EC.element_to_be_clickable(self.third_slide_image)).is_displayed()

    def check_that_the_fourth_image_displayed(self):
        assert self.wait.until(EC.element_to_be_clickable(self.fourth_slide_image)).is_displayed()

    def check_that_the_fifth_image_displayed(self):
        assert self.wait.until(EC.element_to_be_clickable(self.fifth_slide_image)).is_displayed()

    def wait_promotions_popup_to_display(self):
        self.wait.until(EC.element_to_be_clickable(self.promotions_side_button_popup)).is_displayed()

    def check_the_promotions_popup_text(self):
        assert self.browser.find_element(*self.promotion_popup_title).text == 'GRATTEZ ET ÉPARGNEZ!'
        assert self.browser.find_element(*self.promotion_popup_below_the_title).text == 'GRATTEZ POUR VALIDER VOTRE RABAIS!'
        assert self.browser.find_element(*self.promotion_popup_button).text == 'Cliquez pour gratter!'
        self.browser.find_element(*self.textarea_message).text == 'Découvrez instantanément votre offre en grattant! \
            *\n* obtenez la meilleure transaction avec nos rabais'

    def check_the_promotions_popup_fields_to_be_clickable(self):
        self.wait.until(EC.element_to_be_clickable(self.nom_field))
        self.wait.until(EC.element_to_be_clickable(self.courriel_field))
        self.wait.until(EC.element_to_be_clickable(self.telephone_field))
        self.wait.until(EC.element_to_be_clickable(self.vehicule_recherche))

    def check_hyundai_longueuil_link_in_french_language(self):
        self.check_alert_message_in_french_language()
        assert self.browser.current_url == 'https://www.hyundailongueuil.com/'

    def check_alert_message_in_french_language(self):
        assert self.browser.find_element(*self.alert_message).text == \
            'Notre département des Ventes est maintenant ouvert le Samedi!'
