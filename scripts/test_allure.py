import os,sys
sys.path.append(os.getcwd())
import allure
import pytest

from base.base_driver import get_driver


class TestLogin:

    def setup(self):
        self.driver = get_driver()
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="登录")
    def test_login1(self):
        allure.attach('输入用户名', '找到对应的控件并输入')
        print("找到登录输入框")
        allure.attach('输入密码', '找到对应的控件并输入')
        print("找到密码输入框")
        allure.attach('点击登录', '找到对应的控件并输入')
        print("点击登录")
        assert 1

    # @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="登出")
    def test_logout(self):
        if self.driver.get_screenshot_as_file("screenshot.png"):
            with open("screenshot.png","rb") as f:
               allure.attach("allure上传截图",f.read(),"allure.attach_type.PNG")

