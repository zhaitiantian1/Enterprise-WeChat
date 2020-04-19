

from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'true'
desired_caps['dontStopAppOnReset'] = 'true'
# 执行一条测试用例的时候可能不太明显，但是当执行上百条测试用例时，会对整体的自动化测试效率的提升
desired_caps['skipDeviceInitialization'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
# 通过id来定位
driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()

driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('京东')
WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable)
# 为什么要引用两次back呢，因为手动输入搜索框内容后，点击返回，要点击两次才可以返回首页
driver.back()
driver.back()
driver.quit()
