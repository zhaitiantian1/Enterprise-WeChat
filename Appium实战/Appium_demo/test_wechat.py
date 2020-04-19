import yaml
from appium import webdriver
import pytest


class Test_wechat():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('search_data', yaml.safe_load(open("./search_data.yaml")))
    def test_search(self, search_data):
        # 查找通讯录
        el1 = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        el1.click()
        #
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gq_")
        el2.click()
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el3.send_keys(search_data)
        try:
            el4 = self.driver.find_element_by_id("com.tencent.wework:id/de1")
            el4.click()
        except Exception:
            print("没有该联系人：", search_data)
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/aaj")
        el5.click()
        # 发送消息
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
        el6.send_keys("我叫翟困困")
        # 点击发送
        el7 = self.driver.find_element_by_id("com.tencent.wework:id/dtr")
        el7.click()
