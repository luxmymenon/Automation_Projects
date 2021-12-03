from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator
from seletools.actions import drag_and_drop


class Drop_Down_Menu_Element(BasePage):
    url = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def drop_down_elements(self):
        drop_down_ele_locator = (By.ID, "dropdown")
        return BaseElement(driver=self.driver, locator=drop_down_ele_locator)
        # return drop_down_element

    def select_drop_down(self, element):
        drop_down_ele = Select(element)
        return drop_down_ele

