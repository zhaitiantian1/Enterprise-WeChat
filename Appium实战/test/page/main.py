from test.page.basepage import BasePage
from test.page.search import Search


class Main(BasePage):
    def goto_market(self):
        # yaml文件中个是一定要注意，by：id中间有空格，而且id不用加引号，因为本身字典中的key就是字符串格式
        self.steps("../page/main.yaml")
        # com.xueqiu.android:id/tv_search
        # tv_search 这两个定位方式都可以
        return Search(self.driver)
