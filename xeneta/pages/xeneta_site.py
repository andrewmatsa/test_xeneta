from selenium.webdriver.common.by import By

from utils.browser_manager import BrowserManager
from xeneta.pages.dialogs.dialog_base import Dialog
from xeneta.pages import get_site, set_site
from xeneta.pages.careers_page import CareersPage
from xeneta.pages.demopage import DemoPage


class XenetaSite:
    _page_locator = (By.XPATH, './/body')

    @classmethod
    def int_site(cls):
        if get_site() is None:
            BrowserManager.int_driver()
            set_site(XenetaSite())

    @classmethod
    def get_site(cls):
        cls.int_site()
        return get_site()

    @property
    def demo(self):
        return DemoPage(selector=self._page_locator)

    @property
    def careers(self):
        return CareersPage(selector=self._page_locator)

    @property
    def dialog(self):
        return Dialog(selector=self._page_locator)
