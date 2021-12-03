from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.drop_down_page import Drop_Down_Menu_Element
from seletools.actions import drag_and_drop


class Test_Drop_Down_Element(BasePage):

    def test_drop_down_element(self):
        drop_down_element_page = Drop_Down_Menu_Element(self.driver)
        drop_down_element_page.access_url()
        drop_down_select_element = drop_down_element_page.drop_down_elements.find()

        drop_down_element_page.select_drop_down(drop_down_select_element).select_by_visible_text("Option 1")
        print(drop_down_element_page.select_drop_down(drop_down_select_element).first_selected_option)
        # d_d_eles = drop_down_element_page.select_drop_down(drop_down_select_element).first_selected_option
        # d_d_eles.attribute("selected")