# -*- coding: utf-8 -*-
import os, sys

import time

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FileManagerPage(BaseAction):
    # 菜单
    menu_button = By.ID,"com.cyanogenmod.filemanager:id/ab_actions"
    # make_dir = By.ID, "com.cyanogenmod.filemanager:id/two_columns_menu1_item_text"
    make_dir = By.XPATH, ("text,新建文件夹")
    make_file = By.XPATH, ("text,新建文件")
    param = By.XPATH, ("text,属性")
    reflash_button = By.XPATH, ("text,刷新")
    all_select_button = By.XPATH, ("text,全部选择")
    no_all_select_button = By.XPATH,("text,取消全选")
    add_book_button = By.XPATH, ("text,添加到书签")
    add_kj = By.XPATH, ("text,添加快捷方式")
    setashome = By.XPATH, ("text,Set as home")
    cansel = By.XPATH, ("text,取消")

    move_select = By.XPATH, ("text,移动选择项")

    # 新建文件夹,文件
    input_button = By.CLASS_NAME, "android.widget.EditText"
    sure_button = By.XPATH, ("text,确定")
    cansel_button = By.XPATH, ("text,取消")
    # 全选后查看


    # 返回 使用sendkey

    # 当前目录
    current_dir = By.ID,"com.cyanogenmod.filemanager:id/breadcrumb_item"

    #  验证属性文件名
    file_dir_name = By.ID, "com.cyanogenmod.filemanager:id/breadcrumb_item"

    # 文件夹
    aaa = By.XPATH, ("text,aaa")
    zzz = By.XPATH, ("text,zzz")

    # 新建文件夹
    def makedir(self, dirnanme):
        self.click(self.menu_button)
        self.click(self.make_dir)
        self.send_keys(self.input_button, dirnanme)
        cz = By.XPATH, ("text,"+dirnanme)
        if self.find_element(cz):
            self.click(self.cansel)
            self.click(self.cansel)
        else:
            self.click(self.sure_button)

    # 进入aaa文件夹
    def click_aaa(self):
        self.click(self.aaa)

    # 创建文件
    def makefile(self, filename):
        for i in range(5):
            cz = By.XPATH,("text,"+filename + str(i) + ".txt")
            self.click(self.menu_button)
            # self.click(self.make_file)
            self.find_elements(self.make_file)[1].click()
            self.send_keys(self.input_button, filename + str(i)+".txt")
            if self.find_element(cz):
                self.click(self.cansel)
                self.click(self.cansel)
            else:
                self.click(self.sure_button)


    # 选中文件
    def selectfiel(self):
        self.click(self.menu_button)
        self.click(self.all_select)

    # 进入zzz文件夹
    def click_zzz(self):
        self.click(self.zzz)

    # 移动文件
    def movefiles(self):
        if self.is_select:
            self.click(self.menu_button)
            self.click(self.move_select)
        else:
            print("未选择文件")

    def is_select(self):
        select = self.find_element(self.is_select_button)
        if select.text.contains("20"):
            return True
        else:
            return False

    # 返回
    def back_button(self):
        self.back()

    # 刷新
    def reflash(self,first_ele):
        file = By.ID,"com.cyanogenmod.filemanager:id/navigation_view_item_name"
        self.click(self.menu_button)
        self.click(self.reflash_button)
        ele = self.find_element(file)
        if ele.text != first_ele.text:
            assert 0




    check_box = By.ID,"com.cyanogenmod.filemanager:id/navigation_view_item_check"
    # 点击复选框
    def click_checkbox(self,filename):
        ele_filename = By.XPATH,("text,"+filename)
        ele0 = self.find_element(ele_filename)
        eles = self.find_elements(self.check_box)
        for ele in eles:
            if ele.location["y"] == (ele0.location["y"]-20):
                ele.click()
                break
    # 属性
    def click_param(self,filename):
        ele_name = By.XPATH,("text,"+filename)
        self.click(self.menu_button)
        self.click(self.param)
        if self.find_element(ele_name) == None:
            assert 0
        self.click(self.sure_button)

    up_button = By.ID,"android:id/up"
    # 添加书签
    def add_book(self,dir):
        dir = By.XPATH,("text,"+dir)
        self.click(dir)
        self.click(self.menu_button)
        self.click(self.add_book_button)
        self.click(self.up_button)
        if self.find_element(dir):
            assert 1
        else:
            assert 0
        time.sleep(3)
        self.back()

    # 添加快捷方式(文件夹)
    def add_kjfs(self,path):
        paths = path.split("/")
        for pathi in paths:
            self.click((By.XPATH,("text,"+pathi)))
        self.click(self.menu_button)
        self.click(self.add_kj)
        self.home()
        if self.find_element((By.XPATH,("text,"+paths[len(paths)-1]))):
            assert 1
        else:
            assert 0

    application = By.XPATH,("content-desc,应用")
    file_manager = By.XPATH,("text,文件管理器")
    # set as home
    def set_home(self,path):
        paths = path.split("/")
        for pathi in paths:
            self.click((By.XPATH, ("text,"+pathi)))
        self.click(self.menu_button)
        self.click(self.setashome)

    def is_home(self,path):
        paths = path.split("/")
        eles = self.find_elements(self.current_dir)
        text1 = eles[len(eles)-1].text
        text2 = paths[len(paths) - 1]
        if text1 == text2:
            assert 1
        else:
            assert 0
        self.back_home()
    # 还原set as home
    def back_home(self):
        father = By.XPATH,("text,父目录")
        self.click(father)
        self.click(self.menu_button)
        self.click(self.setashome)

    is_select_button = By.ID,"com.cyanogenmod.filemanager:id/navigation_status_selection_label"
    # 全选和取消全选(文件夹)
    def all_select(self,path):
        paths = path.split("/")
        for pathi in paths:
            self.click((By.XPATH, ("text,"+pathi)))
        self.click(self.menu_button)
        self.click(self.all_select_button)
        if self.find_element(self.is_select_button):
            assert 1
        else:
            assert 0
    def no_all_select(self):
        self.click(self.menu_button)
        self.click(self.no_all_select_button)






