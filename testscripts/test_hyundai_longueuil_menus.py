import pytest

from flaky import flaky
from base import Base


@flaky(max_runs=2)
@pytest.mark.usefixtures("_init_pages")
class TestHyundaiLongueuilMenus(Base):

    def test_neufs_autos_accent_2017_menu(self):
        self.home_page.click_neufs_autos_accent_2017_menu()
        self.wait_and_check_promo_banner()
        self.check_make_model_year(expected_make_model_year='Hyundai Accent 2017')
        self.neufs_autos_accent_2017_page.wait_autos_accent_2017_image_to_display()
        self.check_the_car_price(expected_car_price='16,093$')
        self.check_the_car_price_discount(expected_discount='-4,390$')
        self.check_the_car_price_promo(expected_car_price_promo='11,703$')

    def test_neufs_autos_accent_hatchback_2017_menu(self):
        self.home_page.click_neufs_autos_accent_hatchback_2017_menu()
        self.wait_and_check_promo_banner()
        self.check_make_model_year(expected_make_model_year='Hyundai Accent Hatchback 2017')
        self.check_the_car_price(expected_car_price='16,093$')
        self.check_the_car_price_discount(expected_discount='-4,390$')
        self.check_the_car_price_promo(expected_car_price_promo='11,703$')

    def test_neufs_autos_elantra_2018_menu(self):
        self.home_page.click_neufs_autos_elantra_2018_menu()
        self.wait_and_check_promo_banner()
        self.neufs_autos_elantra_2018_page.wait_autos_elantra_2018_image_to_display()
        self.check_make_model_year(expected_make_model_year='Hyundai Elantra 2018')
        self.check_the_car_price(expected_car_price='18,203$')
        self.check_the_car_price_discount(expected_discount='-1,500$')
        self.check_the_car_price_promo(expected_car_price_promo='16,703$')
