from appium.webdriver.common.mobileby import MobileBy

from testenter.page.basepage import BasePage


# from testenter.page.memberinvitepage import MemberInvitePage


class AddresslistPage(BasePage):
    def click_addmember(self):
        from testenter.page.memberinvitepage import MemberInvitePage
        el2 = self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))')
        el2.click()
        return MemberInvitePage(self._driver)
