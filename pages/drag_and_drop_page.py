from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator
from seletools.actions import drag_and_drop


class Drag_Drop_Menu_Element(BasePage):
    url = "https://the-internet.herokuapp.com/drag_and_drop"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def drag_and_drop_element_a(self):
        drag_and_drop_ele_locator = (By.ID, "column-a")
        return BaseElement(driver=self.driver, locator=drag_and_drop_ele_locator)

    @property
    def drag_and_drop_element_b(self):
        drag_and_drop_ele_locator = (By.ID, "column-b")
        return BaseElement(driver=self.driver, locator=drag_and_drop_ele_locator)

    # !!! Did not work !!

    # def drag_and_drop_action_chain(self):
    #     return BaseElement.action_chains_item(self)
    #
    # def drag_drop(self):
    #     drag_and_drop_ele_locator_a = BaseElement(driver=self.driver, locator=(By.ID, "column-a"))
    #     drag_and_drop_ele_locator_b = BaseElement(driver=self.driver, locator=(By.ID, "column-b"))
    #     print(drag_and_drop_ele_locator_a.text)
    #     print(drag_and_drop_ele_locator_b.text)
    #     # ele1 = self.drag_and_drop_element_a()
    #     # ele2 = self.drag_and_drop_element_b()
    #     drag_and_drop(self, drag_and_drop_ele_locator_a, drag_and_drop_ele_locator_b)
