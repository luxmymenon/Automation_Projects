from selenium import webdriver
import pytest

from pages.internet_heroku_app_page import TheInternetHeroKuAppPage
from pages.base_page import BasePage


class Test_Internet_Heroku_App(BasePage):
    @pytest.mark.smoke
    def test_challenging_dom(self):
        # log = self.getLogger()
        internet_challenging_dom_page = TheInternetHeroKuAppPage(self.driver)
        internet_challenging_dom_page.access_url()
        internet_challenging_dom_page.challenging_dom_link.click()
        assert "Challenging DOM" in internet_challenging_dom_page.challenging_dom_page_loaded.text

    def test_a_b_tst(self):
        a_b_tst = TheInternetHeroKuAppPage(self.driver)
        a_b_tst.access_url()
        a_b_tst.a_b_testing_link.click()
        assert "A/B Test" in a_b_tst.a_b_testing_page_loaded.text

    def test_add_remove_element_link(self):
        add_remove_ele = TheInternetHeroKuAppPage(self.driver)
        add_remove_ele.access_url()
        add_remove_ele.add_remove_ele_link.click()
        assert "Add/Remove Elements" in add_remove_ele.add_remove_ele_pg_loaded.text

    @pytest.mark.smoke
    def test_context_menu_element_link(self):
        context_menu_ele = TheInternetHeroKuAppPage(self.driver)
        context_menu_ele.access_url()
        context_menu_ele.context_menu_ele_link.click()
        assert "Context Menu" in context_menu_ele.add_remove_ele_pg_loaded.text

    @pytest.mark.smoke
    def test_drag_and_drop_element_link(self):
        drag_and_drop_ele = TheInternetHeroKuAppPage(self.driver)
        drag_and_drop_ele.access_url()
        drag_and_drop_ele.drag_and_drop_ele_link.click()
        assert "Drag and Drop" in drag_and_drop_ele.drag_and_drop_pg_loaded.text

    @pytest.mark.smoke
    def test_drop_down_element_link(self):
        drop_down_ele = TheInternetHeroKuAppPage(self.driver)
        drop_down_ele.access_url()
        drop_down_ele.drop_down_link.click()
        assert "Dropdown List" in drop_down_ele.drop_down_pg_loaded.text

    @pytest.mark.smoke
    def test_dynamic_control_element_link(self):
        dynamic_control_ele = TheInternetHeroKuAppPage(self.driver)
        dynamic_control_ele.access_url()
        dynamic_control_ele.dynamic_control_ele_link.click()
        assert "Dynamic Controls" in dynamic_control_ele.dynamic_control_pg_loaded.text

    def test_entry_ad_element_link(self):
        entry_ad_ele = TheInternetHeroKuAppPage(self.driver)
        entry_ad_ele.access_url()
        entry_ad_ele.entry_ad_ele_link.click()
        assert "Entry Ad" in entry_ad_ele.entry_ad_pg_loaded.text


