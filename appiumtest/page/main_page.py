# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/10/30 16:56
from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage
from appiumtest.page.connect_page import ContactPage


class MainPage(BasePage):
    _contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact(self):
        self.find_and_click(self._contact_element)
        return ContactPage(self.driver)
