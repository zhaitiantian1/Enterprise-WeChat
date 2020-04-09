from time import sleep

from selenium.webdriver.common.by import By

from Base_page.base_page import BasePage
from Base_page.addmember import Addmember


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def go_to_addmember(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, '.index_service_cnt.js_service_list a:nth-child(1)').click()
        sleep(1)
        return Addmember(self._driver)

    def go_to_login(self):
        pass
