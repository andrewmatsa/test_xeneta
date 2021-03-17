import unittest
from xeneta.pages import get_driver
from xeneta.pages.xeneta_site import XenetaSite


class BaseTest(unittest.TestCase):
    site = XenetaSite.get_site()

    def get_current_url(self):
        return get_driver().current_url

    def navigate_to(self, name):
        print(f'------- Navigating to "{name}"')
        get_driver().get(name)

    @classmethod
    def tearDownClass(cls):
        driver = get_driver()
        driver.close()
