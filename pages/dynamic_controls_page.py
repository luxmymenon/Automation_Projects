from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator
from seletools.actions import drag_and_drop


class Dynamic_Controls_Element(BasePage):
    url = "https://the-internet.herokuapp.com/dynamic_controls"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def dynamic_control_remove_element(self):
        dynamic_control_remove_ele_locator = (By.XPATH, "//button[normalize-space()='Remove']")
        return BaseElement(driver=self.driver, locator=dynamic_control_remove_ele_locator)

    @property
    def dynamic_control_checkbox_element(self):
        dynamic_control_checkbox_ele_locator = (By.XPATH, "//div[@id='checkbox']")
        return BaseElement(driver=self.driver, locator=dynamic_control_checkbox_ele_locator)

    @property
    def dynamic_control_enable_button_element(self):
        dynamic_control_enable_button_locator = (By.XPATH, "//button[normalize-space()='Enable']")
        return BaseElement(driver=self.driver, locator=dynamic_control_enable_button_locator)

    @property
    def dynamic_control_textbox_element(self):
        dynamic_control_textbox_ele_locator = (By.XPATH, "//input[@type='text']")
        return BaseElement(driver=self.driver, locator=dynamic_control_textbox_ele_locator)

    @property
    def dynamic_control_disable_button_element(self):
        dynamic_control_enable_button_locator = (By.XPATH, "//button[normalize-space()='Disable']")
        return BaseElement(driver=self.driver, locator=dynamic_control_enable_button_locator)
