from test.page.basepage import BasePage


class Search(BasePage):
    def search(self, value):
        # com.xueqiu.android:id/search_input_text
        self._params["value"] = value
        self.steps("../page/search.yaml")
