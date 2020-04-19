from time import sleep

from appium import webdriver
import yaml
import pytest
from appium.webdriver.common.mobileby import MobileBy


class Test_deletmem():
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def setup(self):
        pass

    def teardown(self):
        self.driver.quit()

    def teardown_class(self):
        pass

    def test_deletmem(self):
        name = "chenrourou"
        # 查找通讯录
        el1 = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        el1.click()
        el2s = self.driver.find_elements_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{name}").instance(0))')
        print(len(el2s))
        while len(el2s) > 1:
            # 查找成员
            el2 = self.driver.find_element_by_android_uiautomator(
                f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{name}").instance(0))')

            el2.click()
            print(el2.text)
            member = el2.text
            # 点击...
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq0").click()
            sleep(2)
            # 编辑成员
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/axr").click()
            sleep(2)
            # 删除成员
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/drk").click()
            # 点击弹窗中的确定
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b89").click()
            sleep(2)
            # finds = self.driver.find_elements_by_android_uiautomator(
            #     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("测试账号").instance(0))')
            assert member not in self.driver.page_source
        print("已经全部删除")
