from selenium import webdriver
import pytest
import time
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.entry_ad_page import Entry_Ad_Element


class Test_Entry_Ad_Element(BasePage):

    def test_entry_ad_remove_element(self):
        entry_ad_element_page = Entry_Ad_Element(self.driver)
        entry_ad_element_page.access_url()
        entry_ad_close_element = entry_ad_element_page.entry_ad_modal_close_element.find()
        time.sleep(1)
        entry_ad_close_element.click()
        try:
            entry_ad_element_page.entry_ad_modal_element.find()
            not_found = False
        except:
            not_found = True

        assert not_found
