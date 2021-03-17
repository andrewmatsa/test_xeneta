import pytest

from tests import HOSTNAME
from tests.base_test import BaseTest


@pytest.mark.header
@pytest.mark.menu
@pytest.mark.smoke
class Test_001_Verify_Header_Footer_Menus(BaseTest):
    """
    DESCRIPTION: Verify header, footer menus on page
    PRECONDITIONS:
    NAME: Verify header menu
    """
    HOSTNAME = f'{HOSTNAME}/demo'
    menu_item_const = ['Our Customers', 'Platform', 'Resources', 'Company', 'Sign in', 'Book a Meeting']

    def test_000_navigate_to_demo_page(self):
        """
        DESCRIPTION: Open demo page and verify current url
        EXPECTED: /demo page is opened
        """
        self.navigate_to(name=self.HOSTNAME)
        demo_page = self.site.demo
        self.assertTrue(demo_page, msg='Demo page is not opened')
        get_current_url = self.get_current_url()
        self.assertEqual(get_current_url, self.HOSTNAME,
                         msg=f'Current url "{get_current_url}" is not equals to "{self.HOSTNAME}"')

    def test_001_header_menu_items(self):
        """
        DESCRIPTION: Check that menu items
        EXPECTED: Menu items is displayed with order "Our Customers, Platform, Resources, Company, Sign in, Book a Metting"
        """
        menu_items = self.site.demo.header.menu.items_as_ordered_dict
        self.assertTrue(menu_items, 'Can not find menu items')
        self.assertEqual(list(menu_items.keys()), self.menu_item_const,
                         msg=f'{list(menu_items.keys())} is not the same as {self.menu_item_const}')

    def test_002_footer_is_displayed(self):
        """
        DESCRIPTION: Verify footer block below of the page
        EXPECTED: Footer menu block is displayed
        """
        self.site.demo.scroll_to_bottom()
        self.__class__.footer = self.site.demo.footer
        self.assertTrue(self.footer, msg='Can not find footer on page')

        footer_menu = self.footer.footer_menu
        self.assertTrue(footer_menu, msg='Can not find footer menu on page')

    def test_003_footer_menu_social(self):
        """
        DESCRIPTION: Verify footer block with social icons are displayed
        EXPECTED: Social block is visible
        """
        footer_menu = self.footer.social
        self.assertTrue(footer_menu, msg='Can not find footer social block on page')
