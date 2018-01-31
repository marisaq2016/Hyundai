import pytest

from flaky import flaky
from base import Base


@flaky(max_runs=2)
@pytest.mark.usefixtures("_init_pages")
class TestHyundaiLongueuilLinks(Base):

    def test_hyundai_logo_link(self):
        self.home_page.click_hyundai_longueuil_logo()
        self.home_page.check_hyundai_longueuil_link_in_french_language()

    def test_home_icon_link(self):
        self.home_page.click_home_icon_link()
        self.home_page.check_hyundai_longueuil_link_in_french_language()

    def test_neufs_link(self):
        self.home_page.click_neufs_link()
        self.wait_and_check_promo_banner()
        self.neufs_page.check_neufs_link()
