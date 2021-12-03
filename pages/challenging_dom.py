from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from bs4 import BeautifulSoup
from .Locator import Locator


class ChallengingDomPage(BasePage):
    url = "https://the-internet.herokuapp.com/challenging_dom"

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @property
    def baz_button(self):
        baz_button_locator = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
        return BaseElement(driver=self.driver, locator=baz_button_locator)

    def canvas_reader(self, pgee_sourcee):
        challenging_dom_page_soup = BeautifulSoup(pgee_sourcee, "html.parser")
        script_data = challenging_dom_page_soup.find_all("script")
        item = ((str(script_data[6])).splitlines())[4].split("'")[1]
        return item
