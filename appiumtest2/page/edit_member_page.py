# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : edit_member_page.py
# @Author   : Pluto.
# @Time     : 2020/11/4 14:09
from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.base_page import BasePage



class EditMemberPage(BasePage):
    _right_element = (MobileBy.XPATH, "//*[@text='确定']")

    def delete_member(self):
        from appiumtest2.page.search_page import SearchPage
        self.find_by_scroll_and_click("删除成员")
        self.find_and_click(self._right_element)
        return SearchPage(self.driver)