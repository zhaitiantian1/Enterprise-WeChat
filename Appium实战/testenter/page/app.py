from testenter.page.basepage import BasePage
from testenter.page.main import Main
from appium import webdriver


class App(BasePage):
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.LaunchSplashActivity"
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = _package
            desired_caps['appActivity'] = _activity
            desired_caps['noReset'] = 'true'
            desired_caps['dontStopAppOnReset'] = 'true'
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            return self._driver.start_activity(_package, _activity)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):

        return Main(self._driver)
