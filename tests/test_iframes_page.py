from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.iframes_page import IFrames_Element


class Test_Frames_Element(BasePage):

    def test_iframes_element(self):
        iframes_element_page = IFrames_Element(self.driver)
        iframes_element_page.access_url()
        iframe_ele = iframes_element_page.iframe_element
        iframe_edit = iframes_element_page.iframe_editor_element.find()
        iframe_edit.clear()
        iframe_edit.send_keys("Hello")
        assert "Hello" in iframe_edit.text
