from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.dynamic_controls_page import Dynamic_Controls_Element
from seletools.actions import drag_and_drop


class Test_Dynamic_Control_Element(BasePage):

    def test_dynamic_control_remove_element(self):
        dynamic_control_element_page = Dynamic_Controls_Element(self.driver)
        dynamic_control_element_page.access_url()
        dynamic_control_remove_element = dynamic_control_element_page.dynamic_control_remove_element.find()
        dynamic_control_checkbox_element = dynamic_control_element_page.dynamic_control_checkbox_element.find()
        dynamic_control_remove_element.click()
        time.sleep(5)
        if not dynamic_control_checkbox_element:
            assert "Add" in dynamic_control_remove_element

    def test_dynamic_control_enable_element(self):
        dynamic_control_element_page = Dynamic_Controls_Element(self.driver)
        dynamic_control_element_page.access_url()
        dynamic_control_enable_button_element = dynamic_control_element_page.dynamic_control_enable_button_element.find()
        dynamic_control_enable_button_element.click()
        time.sleep(5)
        dynamic_control_textbox_element = dynamic_control_element_page.dynamic_control_textbox_element.find()
        is_enabled_value = dynamic_control_textbox_element.is_enabled()
        # assert is_enabled_value is True
        # assert dynamic_control_textbox_element.is_enabled() is True
        if is_enabled_value:
            dynamic_control_enable_button_element = dynamic_control_element_page.dynamic_control_disable_button_element.find()
            dynamic_control_enable_button_element.click()
            time.sleep(5)
            dynamic_control_textbox_element = dynamic_control_element_page.dynamic_control_textbox_element.find()
            is_enabled_value = dynamic_control_textbox_element.is_enabled()
            # print(is_enabled_value)
            assert is_enabled_value == False



