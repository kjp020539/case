# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os,sys
sys.path.append(os.getcwd())

class BaseAction():

    def __init__(self, driver):
        self.driver = driver

    def xpath_revase_father(self,value):
        xpath = ""
        attrs = value.split(",")
        if len(attrs) == 3 and attrs[2] == "0":
            xpath = "contains(@" + attrs[0] + ",'" + attrs[1] + "')"
        else:
            xpath = "@" + attrs[0] + " = '" + attrs[1]+"'"
        return xpath

    def xpath_revase(self,value):
        xpath = ""
        if isinstance(value,str):
            # 单个值
           xpath = self.xpath_revase_father(value)
        else:
            for para in value:
                xpath = xpath + self.xpath_revase_father(para)+" and "
        xpath = xpath.rstrip(' and ')
        xpath = "//*[" + xpath + "]"
        return xpath

    # 滑动
    def base_swipe(self,act="up"):
        loc = self.driver.get_window_size()
        start_y = loc["height"]*0.25
        end_y = loc["height"]*0.75
        x = loc["width"]*0.5
        if act == "up":
            self.driver.swipe(x,end_y,x,start_y)
        elif act == "down":
            self.driver.swipe(x, start_y, x, end_y)
        else:
            assert 0,"act value error: act should be up or down"

    # 定位单个元素
    def find_element(self, param,timeout=10, poll=1):
        ele = None
        by, value = param
        if by == By.XPATH:
            value = self.xpath_revase(value)
        while True:
            try:
                ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
                break
            except Exception as e:
                self.base_swipe()
        return ele
    # 定位多个元素
    def find_elements(self, param, timeout=10, poll=1):
        eles = None
        by, value = param
        if by == By.XPATH:
            value = "//*[contains(@" + value[0] + ",'" + value[1] + "')]"
        while True:
            try:
                eles = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))
                break
            except Exception as e:
                self.driver.swipe(188, 659, 148, 248)
        return eles


    def click(self,param):
        self.find_element(param).click()

    # 输入
    def send_keys(self,param,value):
        self.find_element(param).clear().send_keys(value)

    # 返回
    def back(self):
        self.driver.keyevent(4)

    def home(self):
        self.driver.keyevent(3)

    def find_toast(self,message,timeout=5):
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        element = WebDriverWait(self.driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
        return element.text