from selenium.webdriver.common.by import By
from xeneta.components.base import ComponentBaseCore


class MenuItem(ComponentBaseCore):
    _name = (By.XPATH, './a')

    @property
    def name(self):
        return self._get_web_element_text(selector=self._name, context=self._we, timeout=3)


class Menu(ComponentBaseCore):
    _item = (By.XPATH, ".//*[contains(@class, 'hs-menu-depth-1')]")
    _list_item_type = MenuItem

    def click_menu_item(self, item_name):
        pass


class Header(ComponentBaseCore):
    _menu = (By.XPATH, ".//*[contains(@class, 'hs-menu-flow-horizontal')]")

    @property
    def menu(self):
        return Menu(selector=self._menu, context=self._we)
