from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .Locator import Locator
from selenium import webdriver
import pytest


class TheInternetHeroKuAppPage(BasePage):
    url = "https://the-internet.herokuapp.com/"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()


    @property
    def challenging_dom_link(self):
        challenging_dom_link = Locator(by=By.CSS_SELECTOR, value="a[href='/challenging_dom']")
        return BaseElement(driver=self.driver, locator=challenging_dom_link)

    @property
    def challenging_dom_page_loaded(self):
        challenging_dom_page_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=challenging_dom_page_loaded)

    @property
    def a_b_testing_link(self):
        a_b_testing_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/abtest']")
        return BaseElement(driver=self.driver, locator=a_b_testing_lnk)

    @property
    def a_b_testing_page_loaded(self):
        a_b_test_page_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=a_b_test_page_loaded)

    @property
    def add_remove_ele_link(self):
        add_remove_element_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/add_remove_elements/']")
        return BaseElement(driver=self.driver, locator=add_remove_element_lnk)

    @property
    def add_remove_ele_pg_loaded(self):
        add_remove_element_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[id='content'] h3")
        return BaseElement(driver=self.driver, locator=add_remove_element_pg_loaded)

    @property
    def context_menu_ele_link(self):
        context_menu_element_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/context_menu']")
        return BaseElement(driver=self.driver, locator=context_menu_element_lnk)

    @property
    def context_menu_pg_loaded(self):
        context_menu_element_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=context_menu_element_pg_loaded)

    @property
    def drag_and_drop_ele_link(self):
        context_menu_element_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/drag_and_drop']")
        return BaseElement(driver=self.driver, locator=context_menu_element_lnk)

    @property
    def drag_and_drop_pg_loaded(self):
        drag_and_drop_element_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=drag_and_drop_element_pg_loaded)

    @property
    def drop_down_link(self):
        drop_down_element_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/dropdown']")
        return BaseElement(driver=self.driver, locator=drop_down_element_lnk)

    @property
    def drop_down_pg_loaded(self):
        drag_and_drop_element_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=drag_and_drop_element_pg_loaded)

    @property
    def dynamic_control_ele_link(self):
        dynamic_control_element_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/dynamic_controls']")
        return BaseElement(driver=self.driver, locator=dynamic_control_element_lnk)

    @property
    def dynamic_control_pg_loaded(self):
        dynamic_control_element_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h4")
        return BaseElement(driver=self.driver, locator=dynamic_control_element_pg_loaded)

    @property
    def entry_ad_ele_link(self):
        entry_ad_element_lnk = Locator(by=By.CSS_SELECTOR, value="a[href='/entry_ad']")
        return BaseElement(driver=self.driver, locator=entry_ad_element_lnk)

    @property
    def entry_ad_pg_loaded(self):
        entry_ad_element_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h3")
        return BaseElement(driver=self.driver, locator=entry_ad_element_pg_loaded)

    @property
    def entry_ad_modal_loaded(self):
        entry_ad_modal_pg_loaded = Locator(by=By.CSS_SELECTOR, value="div[class='example'] h4")
        return BaseElement(driver=self.driver, locator=entry_ad_modal_pg_loaded)

