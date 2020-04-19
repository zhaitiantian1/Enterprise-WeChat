from time import sleep

from testenter.page.app import App
import pytest
import yaml


class TestAddContact():
    # 这里一开始App调用的时候没有加括号，没有加括号相当于调用了App类，但是没有初始化对象，只有对象才能调用方法
    # 另外start方法要加上返回值return self，否则无法调用到main方法
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("name,sex,mobile", yaml.safe_load(
        open("/Users/zhaitiantian3/PycharmProjects/装饰器/testenter/data/contact.yaml")))
    def test_addtact(self, name, sex, mobile):
        l1 = self.main.goto_addresslist().click_addmember().click_memualadd()
        l1.input_name(name).set_gender(sex).input_phone(mobile).click_save().click_back()
