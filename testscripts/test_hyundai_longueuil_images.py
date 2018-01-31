import pytest

from base import Base


@pytest.mark.usefixtures("_init_pages")
class TestHyundaiLongueuilImages(Base):

    def test_first_slide_image_from_home_page(self):
        self.home_page.click_slide_image_from_home_page(nth_expected_image=1)
        self.home_page.check_that_the_first_image_displayed()

    def test_second_slide_image_from_home_page(self):
        self.home_page.click_slide_image_from_home_page(nth_expected_image=2)
        self.home_page.check_that_the_second_image_displayed()

    def test_third_slide_image_from_home_page(self):
        self.home_page.click_slide_image_from_home_page(nth_expected_image=3)
        self.home_page.check_that_the_third_image_displayed()

    def test_fourth_slide_image_from_home_page(self):
        self.home_page.click_slide_image_from_home_page(nth_expected_image=4)
        self.home_page.check_that_the_fourth_image_displayed()

    def test_fifth_slide_image_from_home_page(self):
        self.home_page.click_slide_image_from_home_page(nth_expected_image=5)
        self.home_page.check_that_the_fifth_image_displayed()
