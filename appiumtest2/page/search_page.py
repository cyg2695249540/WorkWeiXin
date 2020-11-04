# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : search_page.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:56
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.base_page import BasePage
from appiumtest2.page.personal_information_page import PersonalInformationPage


class SearchPage(BasePage):
    _search_element = (MobileBy.XPATH, "//*[@text='搜索']")
    _search_result = (MobileBy.ID, "com.tencent.wework:id/ca0")

    def searchmember(self, name):
        search_name = (MobileBy.XPATH, f"//*[@text='{name}']")
        self.find_and_send_keys(self._search_element, name)
        sleep(1)
        eles = self.finds(search_name)
        if len(eles) < 2:
            print("没有该联系人")
        else:
            eles[1].click()
        return PersonalInformationPage(self.driver)

    def search_result(self):
        result = self.find_and_get_text(self._search_result)
        return result
