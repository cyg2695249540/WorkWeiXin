# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : connect_page.py
# @Author   : Pluto.
# @Time     : 2020/10/30 16:57
from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage
from appiumtest.page.invite_member_page import InviteMemberPage
from appiumtest.page.search_page import SearchPage


class ContactPage(BasePage):
    _addmemeber_text = "添加成员"
    _search_element = (MobileBy.ID, "hxw")

    def addmember(self):
        self.find_by_scroll_and_click(self._addmemeber_text)
        return InviteMemberPage(self.driver)

    def goto_secrch_page(self):
        self.find_and_click(self._search_element)
        return SearchPage(self.driver)
