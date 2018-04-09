# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_action import BaseAction
from base.base_driver import get_driver
from pages.filemanager_page import FileManagerPage


def test1():
    driver = get_driver("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
    print(driver.get_window_size())
    # ele = driver.find_element_by_xpath("//*[contains(@text,'aaa')]")
    # print(ele.location)
    # 0,292
    # eles1 = driver.find_elements(By.CLASS_NAME,"android.widget.ImageButton")
    # print(len(eles1))
    eles = driver.find_elements(By.ID,"com.cyanogenmod.filemanager:id/navigation_view_item_check")
    print(len(eles))
    # for ele1 in eles:
    #     if ele1.location["y"] == (ele.location["y"]-20):
    #         ele1.click()




def test():
    # aaa = By.XPATH, ("text", "aaa")
    # make_file = By.XPATH, ("text", "新建文件")
    # android.widget.ImageButton
    # menu_button = By.ID,"com.cyanogenmod.filemanager:id/ab_actions"
    driver = get_driver("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
    # action = BaseAction(driver)
    # action.click(menu_button)
    # action.click(aaa)
    # eles = action.find_elements(By.ID,"com.cyanogenmod.filemanager: id / navigation_view_details_item")
    page = FileManagerPage(driver)
    # page.click_checkbox("aaa")
    # filename = "aaa"
    # page.click_checkbox(filename)
    # page.click_param(filename)
    page.is_home("zzz")

def test2():
    # driver = get_driver("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
    action = BaseAction()
    # xpath = "text,全部选择"
    # print(action.xpath_revase(xpath))
    # xpath = "text,全部选择,0"
    # print(action.xpath_revase(xpath))
    # xpath = "text,全部选择,0","text,全部选择,1"
    # print(action.xpath_revase(xpath))
    xpath = ("text,全部选择,0"), ("text,全部选择")
    print(action.xpath_revase(xpath))


def test0():
    driver = get_driver("com.alpha.lagouapk", ".LagouMainPage")
    print(driver.get_window_size())
    driver.find_element_by_id("com.alpha.lagouapk:id/search_tab_txt").send_keys("测试")

def test_taost():
    # driver = get_driver("com.cyanogenmod.filemanager", ".activities.NavigationActivity")
    driver = get_driver()
    action = BaseAction(driver)
    action.back()
    # print(action.find_toast("再次点击即可退出"))

if __name__ == '__main__':
    # test()
    # test0()
    # test2()
    test_taost()