from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator


class IFrames_Element(BasePage):
    url = "https://the-internet.herokuapp.com/iframe"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def iframe_element(self):
        iframe_ele_locator = (By.ID, "mce_0_ifr")
        iframe_element = BaseElement(driver=self.driver, locator=iframe_ele_locator)
        return BaseElement.iframe_switch_item(iframe_element)

    @property
    def iframe_editor_element(self):
        iframe_editor_ele_locator = (By.ID, "tinymce")
        return BaseElement(driver=self.driver, locator=iframe_editor_ele_locator)
        # return BaseElement.iframe_switch_item(iframe_element)

    # def iframe_switch(self, ele):
    #     return BaseElement.iframe_switch_item(ele)
