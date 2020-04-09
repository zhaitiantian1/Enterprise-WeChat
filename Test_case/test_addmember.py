import pytest
from selenium import webdriver

from Base_page.base_page import BasePage
from Base_page.main import Main


class Test_addmember():
    def setup(self):
        self.main = Main()

    def test_member(self):
        assert self.main.go_to_addmember().addmember()
