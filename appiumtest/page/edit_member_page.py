# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : edit_member_page.py
# @Author   : Pluto.
# @Time     : 2020/11/1 14:48
from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage
from appiumtest.page.search_page import SearchPage


class EditMemberPage(BasePage):
    _right_element = (MobileBy.XPATH, "//*[@text='确定']")

    def delete_member(self):
        self.find_by_scroll_and_click("删除成员")
        self.find_and_click(self._right_element)
        return SearchPage(self.driver)
