import pytest
from tests import HOSTNAME
from tests.base_test import BaseTest


@pytest.mark.services
@pytest.mark.smoke
class Test_001_Verify_Services(BaseTest):
    """
    DESCRIPTION: Verify services on demo page. Three services are displayed with bullets and buttons below
    PRECONDITIONS:
    NAME: Verify three services on demo page
    """
    HOSTNAME = f'{HOSTNAME}/demo'
    services_const = ['WATCH VIDEOS', 'BOOK A MEETING', 'GROUP LIVE DEMO']

    def test_000_precondition(self):
        """
        DESCRIPTION: User on demo page
        EXPECTED: /demo page is opened
        """
        self.navigate_to(name=self.HOSTNAME)
        demo_page = self.site.demo
        self.assertTrue(demo_page, msg='Demo page is not opened')

    def test_001_verify_services(self):
        """
        DESCRIPTION: Verify services block is displayed
        EXPECTED: Watch videos, Book a meeting, Group live demo is displayed
        """
        self.__class__.services = self.site.demo.services.items_as_ordered_dict
        self.assertTrue(self.services, msg='Can not find "Services" block on the page')
        self.assertEqual(list(self.services), self.services_const,
                         msg=f'"{list(self.services)}" is not the same as expected "{self.services_const}"')

    def test_002_verify_watch_videos(self):
        """
        DESCRIPTION: Verify bullet has related icon, and button has correct link
        EXPECTED: 1st bullet is displayed with button bellow and correct link is displayed
        """
        self.site.demo.scroll_to_bottom()
        self.__class__.watch_videos = self.services.get(self.services_const[0])
        button_link = self.watch_videos.button
        self.assertTrue(button_link, msg='Button is not displayed')
        self.watch_videos.button.click()
        get_current_url = self.get_current_url()
        self.assertIn(f'{HOSTNAME}/watchdemos', get_current_url)
        self.test_000_precondition()

    def test_003_perform_click_on_book_a_meeting(self):
        """
        DESCRIPTION: Click on "Schedule now" button
        EXPECTED: Iframe with form is displayed
        """
        self.site.demo.scroll_to_bottom()
        self.__class__.services = self.site.demo.services.items_as_ordered_dict
        self.assertTrue(self.services, msg='Can not find "Services" block on the page')

        schedule_now = self.services.get(self.services_const[1])
        schedule_now.button.click()

        dialog = self.site.dialog.wait_for_dialog()
        self.assertTrue(dialog, msg='Can not find modal window')

    def test_004_click_close_popup(self):
        """
        DESCRIPTION: Click close pop-up
        EXPECTED: Pop-up is closed
        """
        dialog = self.site.dialog.close_dialog()
        self.assertFalse(dialog, msg='Modal window is still displaying')

    def test_005_click_on_group_live_demo(self):
        """
        DESCRIPTION: Click on "SIGN UP HERE" button
        EXPECTED: Iframe with form is displayed
        """
        group_live_demo = self.services.get(self.services_const[2])
        group_live_demo.button.click()

        dialog = self.site.dialog.wait_for_dialog()
        self.assertTrue(dialog, msg='Can not find modal window')

    def test_006_close_grop_live_demo_popup(self):
        """
        DESCRIPTION: Click close pop-up
        EXPECTED: Group live demo modal is closed
        """
        self.test_004_click_close_popup()
