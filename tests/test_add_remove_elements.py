from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from pages.add_remove_elements import Add_Remove_Element


class Test_Add_Remove_Element(BasePage):

    def test_add_remove_button(self):
        add_remove_element_page = Add_Remove_Element(self.driver)
        add_remove_element_page.access_url()
        add_remove_element_page.add_element_button.click()
        assert "Delete" in add_remove_element_page.div_elements.text
        add_remove = add_remove_element_page.add_remove_page_buttons.find_elements()
        # print(len(add_remove))
        for ele in add_remove:
            if ele.text == "Delete":
                ele.click()
        assert "Delete" not in add_remove_element_page.div_elements.text




