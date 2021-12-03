from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.drag_and_drop_page import Drag_Drop_Menu_Element
from seletools.actions import drag_and_drop


class Test_Drag_Drop_Element(BasePage):

    def test_drag_drop_element(self):
        drag_drop_element_page = Drag_Drop_Menu_Element(self.driver)
        drag_drop_element_page.access_url()
        drag_drop_element_1 = drag_drop_element_page.drag_and_drop_element_a.find()
        drag_drop_element_2 = drag_drop_element_page.drag_and_drop_element_b.find()
        assert "A" in drag_drop_element_1.text
        drag_and_drop(self.driver, drag_drop_element_1, drag_drop_element_2)
        assert "B" in drag_drop_element_1.text

        ### !!!!  Below given steps didnt work , had to install seletools
        # drag_drop_element_page.drag_drop()
        # print(drag_drop_element_1.text)
        # drag_drop = drag_drop_element_page.drag_and_drop_action_chain()  # Works
        #
        # drag_drop.drag_and_drop(drag_drop_element_1, drag_drop_element_2).pause(5).perform()

        # drag_drop.click_and_hold(drag_drop_element_1).move_to_element(drag_drop_element_2).release(drag_drop_element_1).click(drag_drop_element_2).perform()

        # drag_drop.drag_and_drop(drag_drop_element_1, drag_drop_element_2).perform()

        # drag_drop_element_page.drag_and_drop_action(drag_drop_element_1, drag_drop_element_2)
        # assert "B" in drag_drop_element_1.text
