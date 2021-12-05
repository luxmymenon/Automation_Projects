from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.frames_page import Frames_Element


class Test_Frames_Element(BasePage):

    def test_iframes_element(self):
        iframes_element_page = Frames_Element(self.driver)
        iframes_element_page.access_url()
        iframes_element_page.frames_iframe_element.click()
        assert "An iFrame" in iframes_element_page.frames_iframe_pg_loaded.text

    def test_nested_frames_element(self):
        nested_frames_element_page = Frames_Element(self.driver)
        nested_frames_element_page.access_url()
        nested_frames_element_page.frames_nested_frame_element.click()
        # assert "An iFrame" in iframes_element_page.frames_iframe_pg_loaded.text

    # def test_nested_frames_element(self):
    #     nested_frames_element_page = Frames_Element(self.driver)
    #     nested_frames_element_page.access_url()
    #     nested_frames_element_page.frames_nested_frame_element.click()

