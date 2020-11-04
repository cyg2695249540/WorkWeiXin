# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : app.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:04
from appium import webdriver

from appiumtest2.page.base_page import BasePage
from appiumtest2.page.main_page import MainPage


class App(BasePage):
    def startapp(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            # caps["platformVersion"] = "6.0"
            # caps["deviceName"] = "127.0.0.1:7555"
            caps["deviceName"] = "Z91QGEWM2258H"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.WwMainActivity"
            # 不清除数据
            caps["noReset"] = True
            # 不重启应用
            caps["dontStopAppOnReset"] = True
            # 等待页面空闲的时间
            caps['settings[waitForIdleTimeout]'] = 1
            # 跳过安装，权限设置等操作
            caps["skipDeviceInitialization"] = True
            # 设置可输入中文
            caps["unicodekeyBoard"] = True
            caps["resetkeyBoard"] = True
            # 自动判断弹框
            caps["autoGrantPermissions"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(3)
        else:
            self.driver.launch_app()
        return self

    def stopapp(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main_page(self):
        return MainPage(self.driver)
