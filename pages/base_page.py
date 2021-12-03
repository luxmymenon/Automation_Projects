import pytest
from selenium import webdriver
import logging


# from tests.conftest import browser_init


@pytest.mark.usefixtures("browser_init")
class BasePage:
    # pass
    # def __init__(self, driver):
    #     self.driver = driver
    #
    def access_url(self):
        self.driver.get(self.url)

    def pge_src(self):
        page_src = self.driver.page_source
        return page_src

    def get_logger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
