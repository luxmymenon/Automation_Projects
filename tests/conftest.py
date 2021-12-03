import pytest
from selenium import webdriver
from utilities.config import Config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome:  ")
    parser.addoption("--env", action="store", help="Environment to test against eg: dev or qa")


@pytest.fixture(scope="class")
def browser_init(request):
    # browser = request.param
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_path = "C:/Users/luxmy/Automation/chromedriver_win32/chromedriver.exe"
        web_driver = webdriver.Chrome(chrome_path)
        # dvr = driver()
    elif browser == "edge":
        edge_path = "C:/Users/luxmy/Automation/edgedriver_win32/msedgedriver.exe"
        web_driver = webdriver.Edge(edge_path)
        # dvr = driver()
    request.cls.driver = web_driver
    return request.cls.driver


def access_url(self):
    self.driver.get(self.url)


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg
