from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestBaidu():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        # cls = self.driver.find_element_by_link_text("设置")
        sleep(2)
        # a="class"
        # assert 'c' in a
        # assert 's_btn_wr' in self.driver.page_source
        # # print(self.driver.page_source)
        cls = self.driver.find_element(By.CSS_SELECTOR, '#u1 >a.pf')

        action = ActionChains(self.driver)
        action.move_to_element(cls)
        action.perform()
        self.driver.find_element(By.CSS_SELECTOR, '.bdpfmenu a:nth-child(3)').click()
        sleep(3)
