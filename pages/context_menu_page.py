from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator


class Context_Menu_Element(BasePage):
    url = "https://the-internet.herokuapp.com/context_menu"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def context_menu_box(self):
        context_menu_box_locator = (By.ID, "hot-spot")
        return BaseElement(driver=self.driver, locator=context_menu_box_locator)
        # new_ele = BaseElement(driver=self.driver, locator=context_menu_box_locator)
        # new_ele.right_click_element()

    def context_menu_alert_ele_txt(self):
        return BaseElement.click_alert_element(self)

    def context_alert_accept(self):
        return BaseElement.accept_alert_element(self)

