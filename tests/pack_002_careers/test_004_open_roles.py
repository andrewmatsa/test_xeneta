import pytest
from tests import HOSTNAME
from tests.base_test import BaseTest


@pytest.mark.careers
@pytest.mark.open_roles
@pytest.mark.smoke
class Test_001_Verify_Open_Roles(BaseTest):
    """
    DESCRIPTION: Verify “Our roles” block with dropdowns and related text inside
    PRECONDITIONS:
    NAME: Verify several dropdowns with text
    """
    def test_000_precondition(self):
        """
        DESCRIPTION: User on career page
        EXPECTED: /career page is opened
        """
        self.navigate_to(name=f'{HOSTNAME}/careers')
        career_page = self.site.careers
        self.assertTrue(career_page, msg='Career page is not opened')

    def test_001_verify_open_roles_is_displayed(self):
        """
        DESCRIPTION: Verify open roles is displayed
        EXPECTED: Block is displayed
        """
        self.site.careers.scroll_to_bottom()
        self.__class__.open_roles = self.site.careers.open_roles
        self.assertTrue(self.open_roles, msg='Open roles is not displayed')

    def test_002_verify_dropdown_list_with_collapse_and_expand_state(self):
        """
        DESCRIPTION: Verify_dropdown list with collapse and expand
        EXPECTED: Dropdown list is expanded with corresponding text inside
        EXPECTED: Dropdown list is collapsed corresponding text is gone
        """
        open_roles_items = self.open_roles.items_as_ordered_dict
        self.assertTrue(open_roles_items, msg='Open roles accordions is not displayed')
        open_roles_items.items()
        for k, value in open_roles_items.items():
            value.click()
            expanded = value.is_expanded(expected_result=True)
            self.assertTrue(expanded, msg='Section is not expanded')
            value.click()
            expanded = value.is_expanded(expected_result=False)
            self.assertFalse(expanded, msg='Section is still expanded')
