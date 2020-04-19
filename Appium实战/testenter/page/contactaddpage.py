from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from testenter.page.basepage import BasePage


# from testenter.page.memberinvitepage import MemberInvitePage


class ContactAddPage(BasePage):
    def input_name(self, name):
        # 没有完成跳转，return self就可以了
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(
            name)
        print("ok")
        return self

    def set_gender(self, sex):
        # self.steps("../")
        self.find(MobileBy.ID, 'com.tencent.wework:id/ate').click()
        # 注意引号外面要加f
        self.find(MobileBy.XPATH, f"//*[@text='{sex}']").click()
        return self

    def input_phone(self, mobile):
        self.find(MobileBy.ID, 'com.tencent.wework:id/emh').send_keys(mobile)
        return self

    def click_save(self):
        from testenter.page.memberinvitepage import MemberInvitePage
        self.find(MobileBy.ID, 'com.tencent.wework:id/gq7').click()
        return MemberInvitePage(self._driver)
