# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : search_page.py
# @Author   : Pluto.
# @Time     : 2020/11/1 14:38
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage
from appiumtest.page.personal_information_page import PersonalInformationPage


class SearchPage(BasePage):
    _search_element = (MobileBy.XPATH, "//*[@text='搜索']")
    _search_name = (MobileBy.XPATH, "//*[@text='LCQ']")

    def searchcontact(self):
        self.find_and_send_keys(self._search_element, "LCQ")
        sleep(1)
        eles = self.finds(self._search_name)
        if len(eles) <2:
            print("没有该联系人")
        else:
            eles[1].click()
        return PersonalInformationPage(self.driver)

    def get_result(self):
        self.find_and_get_text()