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

    # 定位单个元素
    def find_element(self, param, timeout=10, poll=1):
        ele = None
        by, value = param
        if by == By.XPATH:
            value = "//*[contains(@" + value[0] + ",'" + value[1] + "')]"
        while True:
            try:
                ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
                break
            except Exception as e:
                self.driver.swipe(188, 659, 148, 248)
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