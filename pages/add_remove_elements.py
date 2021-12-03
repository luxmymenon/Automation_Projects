from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator


class Add_Remove_Element(BasePage):
    url = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def add_element_button(self):
        add_element_button_locator = (By.XPATH, "//button[@onclick='addElement()']")
        return BaseElement(driver=self.driver, locator=add_element_button_locator)

    @property
    def div_elements(self):
        div_elements = (By.ID, "elements")
        return BaseElement(driver=self.driver, locator=div_elements)

    @property
    def add_remove_page_buttons(self):
        add_remove_page_buttons_list = (By.XPATH, "//button")
        return BaseElement(driver=self.driver, locator=add_remove_page_buttons_list)

    # @property
    # def remove_element_button(self):
    #     remove_element_button_locator = (By.XPATH, "//button")
    #     return BaseElement(driver=self.driver, locator=remove_element_button_locator)
