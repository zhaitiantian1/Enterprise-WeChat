import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = None
        # 如果发现driver没有值，说明第一次实例化子类
        if self._driver is None:
            ops_chrome = webdriver.ChromeOptions()
            ops_chrome.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=ops_chrome)
            # 如果发现有值，说明不是第一次实例化子类，就把driver传递下去
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(5)

    def find(self, by, locate):
        return self._driver.find_element(by, locate)
