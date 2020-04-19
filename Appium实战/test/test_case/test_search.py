from test.page.app import App
from test.page.basepage import BasePage


class Test_search():

    def test_search(self):
        App().start().main().goto_market().search("jd")
