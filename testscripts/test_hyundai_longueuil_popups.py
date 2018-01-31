import pytest

from base import Base


@pytest.mark.usefixtures("_init_pages")
class TestHyundaiLongueuilPopups(Base):

    def test_promotions_side_button_popup(self):
        self.home_page.click_promotions_side_button()
        self.home_page.check_the_promotions_side_button_popup()

    def test_textez_nous_side_button_popup(self):
        self.home_page.click_textez_nous_side_button()
        self.home_page.check_textez_nous_popup()
