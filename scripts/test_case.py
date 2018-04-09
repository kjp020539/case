# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.getcwd())
from base.base_driver import get_driver
from pages.filemanager_page import FileManagerPage
from selenium.webdriver.common.by import By
import pytest
import allure
class TestCase():

    """
    before方法和setup功能一样
    """
    @pytest.fixture(scope="function")
    def before(self):
        # 进入文件管理器
        self.driver = get_driver("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
        self.page = FileManagerPage(self.driver)
        file = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"
        self.first_ele = self.page.find_element(file)
    @pytest.mark.skipif(condtion=True)
    def setup(self):
        # 进入文件管理器
        self.driver = get_driver("com.cyanogenmod.filemanager",".activities.NavigationActivity")
        self.page = FileManagerPage(self.driver)
        file = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"
        self.first_ele = self.page.find_element(file)

    # def test_movefile(self):
    #     # 新建aaa文件夹
    #     self.page.makedir("aaa")
    #
    #     # 创建zzz文件夹
    #     self.page.makedir("zzz")
    #
    #     # 刷新
    #     self.page.reflash(self.first_ele)
    #
    #     # 进入aaa文件夹
    #     self.page.click_aaa()
    #
    #     # 创建文件
    #     self.page.makefile("test")
    #
    #     # 选中文件
    #     self.page.selectfiel()
    #
    #     # 返回
    #     self.page.back_button()
    #     self.page.reflash(self.first_ele)
    #
    #     # 进入zzz文件夹
    #     self.page.click_zzz()
    #
    #     # 移动文件
    #     self.page.movefiles()

    # 验证文件属性名
    # def test_patam(self):
        filename = "aaa"
        self.page.click_checkbox(filename)
        self.page.click_param(filename)

    # 刷新
    # def test_refrash(self):
    #     self.page.reflash(self.first_ele)

    # # 添加文件夹到书签
    # def test_book(self):
    #     self.page.add_book("aaa")

    # 添加快捷方式
    def test_kjfs(self):
        path = "zzz"
        self.page.add_kjfs(path)

    # home_path = "zzz"
    # # set as home(文件夹)
    # def test_setashome(self):
    #     self.page.set_home(self.home_path)
    # def test_is_setashome(self):
    #     self.page.is_home(self.home_path)


    # 全选和取消全选
    @allure.step("测试步骤")
    def test_select(self):
        allure.attach()
        dir = "zzz"
        self.page.all_select(dir)
        self.page.no_all_select()