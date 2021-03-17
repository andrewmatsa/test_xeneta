from selenium.webdriver.common.by import By
from xeneta.components.base import ComponentBaseCore
from xeneta.primitives.buttons import Buttons


class DialogContent(ComponentBaseCore):
    _close_button = (By.XPATH, ".//*[@class='close-modal ']")

    @property
    def close_button(self):
        return Buttons(selector=self._close_button, context=self._we)


class Dialog(ComponentBaseCore):
    _dialog = (By.XPATH, ".//*[@class='jquery-modal blocker current']")
    _dialog_type = DialogContent

    @property
    def dialog(self):
        context = self._dialog_type(selector=self._dialog, context=self._we, timeout=1)
        return context

    def wait_for_dialog(self):
        return self.dialog

    def close_dialog(self):
        self.dialog.close_button.click()
        self.wait_dialog_closed()

    def wait_dialog_closed(self, timeout=5):
        self._element_is_not_displayed(selector=self._dialog, timeout=timeout)
