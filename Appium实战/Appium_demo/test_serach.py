from appium import webdriver
import pytest


class Test_search():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        # 默认为英文输入法，将输入法改为中文
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tear_down(self):
        pass

    pytest.mark.parametrize('search,type,expected_price', )

    def test_xueqiusearch(self):
        """
        1.打开雪球应用
        2.点击搜索框
        3.输入搜索词’京东’或者’小米“
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()

        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('京东')
