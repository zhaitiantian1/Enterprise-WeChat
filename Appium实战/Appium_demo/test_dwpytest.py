import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_xueqiu:
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

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    # @pytest.mark.skip
    def test_xueqiu(self):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.想搜索框中输入京东
        4.在搜索结果里面选择京东，然后进行点击
        5.获取京东股价，并判断这只股价的价格大于
        :return:
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()

        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('京东')
        # 这里必须要添加双引号，因为里面有单引号
        # lacator = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='京东']")
        # # 显式等待
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(lacator))
        # ele = self.driver.find_element(*lacator)
        # print(ele.text)

        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='京东']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 40

    def test_attr(self):
        """
        1.打开雪球应用首页
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和它的宽高
        5.想搜索框输入：京东
        6.判断【京东】是否可见
        7.如果可见，打印"搜索成功"点击，如果不可见，打印搜素失败
        :return:
        """
        elem = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        search_enabled = elem.is_enabled()
        print(elem.text)
        print(elem.location)
        print(elem.size)
        if search_enabled == True:
            elem.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('京东')
            jd_elem = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='京东']")
            # 打印的是一个字符串的True，不是bool值，get_attibute的所有属性都可以获取到
            print(jd_elem.get_attribute('displayed'))
            elem_display = jd_elem.get_attribute('displayed')
            if elem_display == 'true':
                print('搜索成功')
            else:
                print('搜索失败')

    def test_action(self):
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        heigt = window_rect['height']
        x1 = int(width / 2)
        y_start = int(heigt * 4 / 5)
        y_end = int(heigt * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_price(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()

        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        # 这里必须要添加双引号，因为里面有单引号
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        lacator = (MobileBy.XPATH, "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 显式等待
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(lacator))
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*lacator))
        # ele = self.driver.find_element(*lacator)
        print(ele.text)
        current_price = float(ele.text)
        # current_price = self.driver.find_element_by_xpath(
        #     "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        # 这里是float类型不要用int，因为是价格
        assert float(current_price) > 150

    def test_login(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()

    def test_scroll(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("雪盈福利").instance(0))').click()
