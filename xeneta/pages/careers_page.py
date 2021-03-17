from selenium.webdriver.common.by import By

from xeneta.components.base import ComponentBaseCore
from xeneta.pages.base_page import BasePage
from xeneta.primitives.buttons import Buttons


class IndustryTabContent(ComponentBaseCore):
    _image = (By.XPATH, ".//img")
    _text = (By.XPATH, ".//h2")

    @property
    def image(self):
        self.scroll_to_bottom()
        return Buttons(selector=self._image, context=self._we, timeout=5)

    @property
    def text(self):
        return self._get_web_element_text(selector=self._text, context=self._we)


class TabsMenuItem(ComponentBaseCore):
    _item = (By.XPATH, ".//*[contains(@class, 'tab-link')]")
    _list_item_type = Buttons
    _menu_item = (By.XPATH, ".//*[contains(@class, 'tab-link  current')]")

    @property
    def current(self):
        return self._get_web_element_text(selector=self._menu_item, context=self._we)

    @property
    def name(self):
        return self.current.text


class Industry(ComponentBaseCore):
    _tabs = (By.XPATH, ".//*[@class='tabs']")
    _tabs_type = TabsMenuItem
    _tab_content = (By.XPATH, ".//*[contains(@class, 'tab-content') and contains(@class, 'current')]")
    _tab_content_type = IndustryTabContent

    @property
    def tabs_menu(self):
        return self._tabs_type(selector=self._tabs)

    @property
    def tab_content(self):
        return self._tab_content_type(selector=self._tab_content)


class Accordion(ComponentBaseCore):
    _name = (By.XPATH, ".//h4")
    _expanded = (By.XPATH, ".//*[contains(@class, 'accordion_group') and contains(@class, 'expanded')]")

    @property
    def text(self):
        return self._get_web_element_text(selector=self._name, context=self._we)

    @property
    def name(self):
        return self.text

    def is_expanded(self, timeout=5, expected_result=True):
        if expected_result:
            result = self._get_web_element_text(selector=self._expanded, context=self._we, timeout=timeout)
        if not expected_result:
            result = self._element_is_not_displayed(selector=self._expanded)
            if result == True:
                result = False
        return bool(result)


class OpenRoles(ComponentBaseCore):
    _item = (By.XPATH, ".//*[@class='acdn-heading']")
    _list_item_type = Accordion


class CareersPage(BasePage):
    _industry = (By.XPATH, ".//*[@class='industry-inner']")
    _industry_type = Industry
    _open_roles = (By.XPATH, ".//*[@class='subscription-model-inner']")
    _open_roles_type = OpenRoles

    @property
    def industry(self):
        return self._industry_type(selector=self._industry)

    @property
    def open_roles(self):
        return self._open_roles_type(selector=self._open_roles)


