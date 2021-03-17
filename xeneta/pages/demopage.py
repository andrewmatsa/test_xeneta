from selenium.webdriver.common.by import By

from xeneta.components.base import ComponentBaseCore
from xeneta.pages.base_page import BasePage
from xeneta.primitives.buttons import Buttons


class ServicesItem(ComponentBaseCore):
    _name = (By.XPATH, ".//h3")
    _button = (By.XPATH, ".//*[@class='popup-btn'] | .//*[@class='cta_button ']")

    @property
    def name(self):
        return self._get_web_element_text(selector=self._name, context=self._we)

    @property
    def button(self):
        return Buttons(selector=self._button, context=self._we)


class Services(ComponentBaseCore):
    _item = (By.XPATH, ".//*[@class='hs_cos_wrapper']")
    _list_item_type = ServicesItem


class DemoPage(BasePage):
    _services = (By.XPATH, "(.//*[contains(@class,'three-col-bullets')])[2]")
    _services_type = Services

    @property
    def services(self):
        return self._services_type(selector=self._services, context=self._we)
