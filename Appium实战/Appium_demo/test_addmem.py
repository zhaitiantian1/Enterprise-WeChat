from time import sleep

from appium import webdriver
import yaml
import pytest
from appium.webdriver.common.mobileby import MobileBy


class Test_addmem():
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
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gpp').click()

    def teardown_class(self):
        self.driver.quit()
    #注意这里参数必须要加双引号，加单引号会报错
    @pytest.mark.parametrize("mobile,name,sex", [('17801153312', '测试账号12', '男'), ('17801153311', '测试账号11', '女')])
    def test_search(self, mobile, name, sex):
        # 查找通讯录
        el1 = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        el1.click()
        # 添加成员
        el2 = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))')
        el2.click()
        # self.driver.find_element_by_id('com.tencent.wework:id/c56')

        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/c56').click()
        sleep(2)
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(
            name)
        # 输入手机号
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/emh').send_keys(mobile)
        # 选择性别
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ate').click()
        #注意引号外面要加f
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{sex}']").click()
        # 点击保存
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gq7').click()
        # print(self.driver.page_source)
        # self.driver.find_element(MobileBy.XPATH, "//*['@text=添加成功']")
        sleep(2)  #
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' in toast
