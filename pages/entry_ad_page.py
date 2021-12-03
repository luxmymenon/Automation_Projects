from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator
from seletools.actions import drag_and_drop


class Entry_Ad_Element(BasePage):
    url = "https://the-internet.herokuapp.com/entry_ad"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def entry_ad_modal_element(self):
        entry_ad_modal_ele_locator = (By.CSS_SELECTOR, "div[class='modal-title'] h3")
        return BaseElement(driver=self.driver, locator=entry_ad_modal_ele_locator)

    @property
    def entry_ad_modal_close_element(self):
        entry_ad_modal_close_ele_locator = (By.CSS_SELECTOR, "div[class='modal-footer'] p")
        return BaseElement(driver=self.driver, locator=entry_ad_modal_close_ele_locator)