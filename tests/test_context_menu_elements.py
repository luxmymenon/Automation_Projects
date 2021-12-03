from pages.base_page import BasePage
from pages.context_menu_page import Context_Menu_Element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_Context_Menu_Page_Element(BasePage):

    def test_context_menu_items(self):
        context_menu_items_page = Context_Menu_Element(self.driver)
        context_menu_items_page.access_url()
        context_menu_items_page.context_menu_box.right_click_element()
        alert_text = context_menu_items_page.context_menu_alert_ele_txt().text
        assert "You selected a context menu" in alert_text
        context_menu_items_page.context_menu_alert_ele_txt().accept()


        # context_menu_box_item = context_menu_items_page.context_menu_box.find()
        # print(type(context_menu_box_item))
        # context_menu_action_chains = ActionChains(context_menu_items_page)
        # context_menu_action_chains.move_to_element(context_menu_box_item)
        # context_menu_action_chains.context_click().perform()





