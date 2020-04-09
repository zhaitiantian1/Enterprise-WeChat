import time

from selenium.webdriver.common.by import By

from Base_page.base_page import BasePage


class Addmember(BasePage):
    def addmember(self):
        self.find(By.ID, 'username').send_keys("chenrourou")
        self.find(By.ID, 'memberAdd_acctid').send_keys('12345')
        self.find(By.ID, 'memberAdd_phone').send_keys('18811368458')
        time.sleep(2)
        self.find(By.LINK_TEXT, '保存')


def test_dict():
    d = {'b': 1, 'a': 2, 'c': 10}
    print(d.items())


test_dict()
