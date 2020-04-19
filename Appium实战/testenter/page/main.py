from testenter.page.addresslistpage import AddresslistPage
from testenter.page.basepage import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        self.steps("/Users/zhaitiantian3/PycharmProjects/装饰器/testenter/steps/mainwe.yaml")

        return AddresslistPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_myprofile(self):
        pass
