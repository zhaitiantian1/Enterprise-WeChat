import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import yaml
from selenium.webdriver.common.by import By


class BasePage():
    logging.basicConfig(level=logging.INFO)
    _black_list = [MobileBy.ID, 'image_cancel']
    _error_count = 0
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        # *by意思是传递多个位置参数,如果传递的是一个元组的话，就用前面的,locator注意默认等于None
        logging.info(locator)
        try:
            self._error_count = 0
            return self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
                raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(by, locator)
                raise e

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 注意是list[]而不是list(),因为
            steps: list[dict] = yaml.safe_load(f)
            print(steps)
            for step in steps:
                if "by" in step.keys():
                    if "id" == step["by"]:
                        element = self.find(step["by"], step["locator"])
                    if "xpath" == step["by"]:
                        element = self.find(MobileBy.XPATH, step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self._params:
                            # 如果字典中的值命中了{value}就把param中的值替换了，这就是为什么_params={}设置为字典的原因
                            content = content.replace("{%s}" % param, self._params[param])
                            self.send(content, step["by"], step["locator"])
