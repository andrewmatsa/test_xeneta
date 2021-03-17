from selenium.webdriver.common.by import By
from xeneta.components.base import ComponentBaseCore
from xeneta.components.footer import Footer
from xeneta.components.header import Header


class BasePage(ComponentBaseCore):
    _header = (By.XPATH, ".//*[contains(@class, 'xeneta-header')]")
    _header_type = Header
    _footer = (By.XPATH, ".//*[@class='footer-container-wrapper']")
    _footer_type = Footer

    @property
    def header(self):
        return self._header_type(selector=self._header, context=self._we)

    @property
    def footer(self):
        return self._footer_type(selector=self._footer, context=self._we)
