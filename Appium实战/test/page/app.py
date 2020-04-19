from time import sleep

from test.page.basepage import BasePage
from appium import webdriver

from test.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = "com.xueqiu.android.common.MainActivity"
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = _package
            desired_caps['appActivity'] = _activity
            # desired_caps['autoGrantPermissions'] = 'true'
            # desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            sleep(2)
            self.driver.implicitly_wait(5)
        else:
            return self.driver.start_activity(_package, _activity)
        return self

    def main(self):

        return Main(self.driver)
