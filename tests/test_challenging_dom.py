from selenium import webdriver
import pytest
from pages.base_page import BasePage
from pages.challenging_dom import ChallengingDomPage


@pytest.mark.ui
class Test_Challenging_Dom(BasePage):

    def test_challengin_dom(self):
        c_d_page = ChallengingDomPage(self.driver)
        c_d_page.access_url()
        p_s = c_d_page.pge_src()
        first_value = c_d_page.canvas_reader(p_s)
        # print(c_d_page.baz_button.attribute("text"))
        c_d_page.baz_button.click()
        p_s = c_d_page.pge_src()
        # print(c_d_page.baz_button.attribute("text"))
        after_click_value = c_d_page.canvas_reader(p_s)
        assert first_value != after_click_value
