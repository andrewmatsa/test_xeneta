from xeneta.components.base import ComponentBaseCore


class Buttons(ComponentBaseCore):

    @property
    def href(self):
        return self.get_attribute('href')

    @property
    def src(self):
        return self.get_attribute('src')

    @property
    def name(self):
        return self._we.text