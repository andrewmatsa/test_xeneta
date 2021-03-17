import pytest
from tests import HOSTNAME
from tests.base_test import BaseTest


@pytest.mark.careers
@pytest.mark.our_values
@pytest.mark.smoke
class Test_001_Verify_Our_Values(BaseTest):
    """
    DESCRIPTION: Verify “Our values” block with switchers on careers page.
    PRECONDITIONS:
    NAME: Verify several tabs on page with related content and image
    """
    tabs_constants = ['Xeneta is one', 'Modernization through data', 'Variety and Fairness', 'Transparency builds Trust']


    def test_000_precondition(self):
        """
        DESCRIPTION: User on career page
        EXPECTED: /career page is opened
        """
        self.navigate_to(name=f'{HOSTNAME}/careers')
        career_page = self.site.careers
        self.assertTrue(career_page, msg='Career page is not opened')

        get_current_url = self.get_current_url()
        self.assertEqual(get_current_url, f'{HOSTNAME}/careers',
                         msg=f'Current url "{get_current_url}" is not equals to f"{HOSTNAME}/careers"')

    def test_001_verify_our_values_block_is_displayed(self):
        """
        DESCRIPTION: Verify our values block is displayed
        EXPECTED: Section is displayed
        """
        self.__class__.our_values = self.site.careers.industry
        self.assertTrue(self.our_values, msg='Our Values section is displayed')

    def test_002_verify_that_switchers_has_correct_order(self):
        """
        DESCRIPTION: Verify our values block is displayed
        EXPECTED: Xeneta is one, Modernization through data, Variety and Fairness, Transparency builds Trust
        EXPECTED: Switchers are visible and has correct order
        """
        self.__class__.tabs = self.our_values.tabs_menu.items_as_ordered_dict
        self.assertTrue(self.tabs, msg='Our values tabs is not displayed')
        self.assertEqual(list(self.tabs.keys()), self.tabs_constants,
                         msg=f'Current tabs "{list(self.tabs.keys())}" '
                             f'is not the same as expected "{self.tabs_constants}"')

    def test_003_verify_related_text_and_image_on_different_tabs(self):
        """
        DESCRIPTION: "Xeneta is one" menu item is highlighted by default
        EXPECTED: "Xeneta is one" menu is highlighted
        """
        default_menu_item = self.our_values.tabs_menu.current
        self.assertEqual(default_menu_item, self.tabs_constants[0],
                         msg=f'Current tabs "{default_menu_item}" '
                             f'is not the same as expected "{self.tabs_constants[0]}"')

    def test_004_verify_text_and_image_for_related_tab(self):
        """
        DESCRIPTION: "Xeneta is one" is highlighted and tab content with data is displayed
        EXPECTED: Image and text is displayed for related tab
        """
        image = self.our_values.tab_content.image.src
        self.assertIn('one.png', image, msg=f'Image with .png format is not displayed in "{image}"')
        text = self.our_values.tab_content.text
        self.assertEqual(text, 'Xeneta is One',
                         msg=f'Current tabs "{text}" '
                             f'is not the same as expected "Xeneta is One"')

    def test_005_verify_text_and_image_anoter_tabs(self):
        """
        DESCRIPTION: Click on different tabs and check images and text
        EXPECTED: Image and text is displayed
        """
        for name, tab in self.tabs.items():
            tab.click()
            image = self.our_values.tab_content.image.src
            self.assertIn('.png', image, msg=f'Image with .png format is not displayed in "{image}"')
            if name == 'Xeneta is one':
                name = 'Xeneta is One'
            text = self.our_values.tab_content.text
            self.assertEqual(text, name,
                             msg=f'Current tabs "{text}" '
                                 f'is not the same as expected "{name}')

