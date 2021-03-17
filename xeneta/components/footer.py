from selenium.webdriver.common.by import By
from xeneta.components.base import ComponentBaseCore


class Footer(ComponentBaseCore):
    _social_block = (By.XPATH, ".//*[contains(@class, 'social-icons')]")
    _footer_menu = (By.XPATH, ".//*[contains(@class, 'hs-menu-wrapper')]")

    @property
    def social(self):
        return self._find_element_by_selector(selector=self._social_block, context=self._we) is not None

    @property
    def footer_menu(self):
        return self._find_element_by_selector(selector=self._footer_menu, context=self._we) is not None
