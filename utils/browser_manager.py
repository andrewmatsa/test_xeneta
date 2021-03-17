from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests import HOSTNAME
from xeneta.pages import set_driver


class BrowserManager:
    @classmethod
    def int_driver(cls):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        set_driver(driver)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('window-size=1024x768')
        driver.maximize_window()
        driver.get(HOSTNAME)

