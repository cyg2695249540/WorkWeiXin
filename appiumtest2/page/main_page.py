# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:05
from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.base_page import BasePage
from appiumtest2.page.contact_page import ContactPage


class MainPage(BasePage):
    _contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact_page(self):
        self.find_and_click(self._contact_element)
        return ContactPage(self.driver)
