# from testenter.page.addresslistpage import AddresslistPage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from testenter.page.basepage import BasePage


# from testenter.page.contactaddpage import ContactAddPage


class MemberInvitePage(BasePage):
    def click_memualadd(self):
        from testenter.page.contactaddpage import ContactAddPage
        self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/c56').click()
        return ContactAddPage(self._driver)

    def click_back(self):
        from testenter.page.addresslistpage import AddresslistPage
        sleep(2)
        self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gpp').click()
        return AddresslistPage(self._driver)
