from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator



class Frames_Element(BasePage):
    url = "https://the-internet.herokuapp.com/frames"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def frames_nested_frame_element(self):
        nested_frame_ele_locator = (By.CSS_SELECTOR, "a[href='/nested_frames']")
        return BaseElement(driver=self.driver, locator=nested_frame_ele_locator)

    @property
    def frames_nested_frame_pg_loaded(self):
        nested_frame_ele_locator = (By.CSS_SELECTOR, "div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=nested_frame_ele_locator)

    @property
    def frames_iframe_element(self):
        iframe_ele_locator = (By.CSS_SELECTOR, "a[href='/iframe']")
        return BaseElement(driver=self.driver, locator=iframe_ele_locator)

    @property
    def frames_iframe_pg_loaded(self):
        iframe_ele_locator = (By.CSS_SELECTOR, "div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=iframe_ele_locator)



