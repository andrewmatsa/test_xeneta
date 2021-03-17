from collections import OrderedDict

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from xeneta.pages import get_driver


class ComponentBaseCore(object):
    _item = None
    _list_item_type = None
    _context_timeout = 10

    def __init__(self, selector='', context=None, web_element=None, timeout=_context_timeout):
        self._driver = get_driver()
        self._selector = selector
        self._timeout = timeout
        self._context = context if context is not None else get_driver()
        self._we = web_element or self._find_element_by_selector(selector, self._context)

    def _find_element_by_selector(self, selector='', context=None, timeout=10):
        try:
            element = context.find_element(*selector)
        except (NoSuchElementException, WebDriverException):
            element = WebDriverWait(self._driver, timeout).until(ec.presence_of_element_located(selector),
                                                                 message=f"Can't find element by locator {selector}")
        return element

    def _find_elements_by_selector(self, selector='', context=None, timeout=10):
        try:
            elements = context.find_elements(*selector)
        except (NoSuchElementException, WebDriverException):
            elements = WebDriverWait(self._driver, timeout).until(ec.presence_of_all_elements_located(selector),
                                                                  message=f"Can't find elements by locator {selector}")
        if elements is None:
            return []
        return elements

    def _get_web_element_text(self, selector='', context=None, timeout=10):
        element = self._find_element_by_selector(selector, context, timeout)
        return element.text

    def _element_is_not_displayed(self, selector='', timeout=10):
        element = WebDriverWait(self._driver, timeout).until(ec.invisibility_of_element_located(selector),
                                                                 message=f"Element still displaying {selector}")
        return element

    @property
    def items_as_ordered_dict(self):
        items_we = self._find_elements_by_selector(selector=self._item, context=self._we, timeout=10)
        items_ordered_dict = OrderedDict()
        for item_we in items_we:
            list_item = self._list_item_type(web_element=item_we)
            items_ordered_dict.update({list_item.name: list_item})
        return items_ordered_dict

    def click(self):
        get_driver().implicitly_wait(3)
        self._we.click()

    def get_attribute(self, attribute):
        result = self._we.get_attribute(attribute)
        return result

    def scroll_to_bottom(self):
        drv = get_driver()
        drv.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    # TODO scroll to webelement using js
    # def scroll_to_we(self, web_element=None):
    #     if web_element is None:
    #         web_element = self._we



