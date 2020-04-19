from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import close_to, contains_string,assert_that
# from hamcrest.core import assert_that, equal_to

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_xueqiualert:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:5555'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'  # 不要加apis/.view.
        desired_caps['uiautomationName'] = 'uiautomator2'
        sleep(2)
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(10)

    # @pytest.mark.skip
    # def teardown(self):
    #     self.driver.quit()
    #
    # @pytest.mark.skip
    # def test_toast(self):
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='Make a Popup!']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
    #     # print(self.driver.page_source)
    #     print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
    #     # 注意这个元素定位，contains
    #     print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup menu')]").text)

    def test_assert(self):
        # assert_that(10, equal_to(10), '这是一个提示')
        # assert_that(8, close_to(10, 2))
        assert_that('hello,rourou', contains_string('rourou'))
