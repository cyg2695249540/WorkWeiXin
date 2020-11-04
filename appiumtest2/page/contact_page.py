# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:05
from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.base_page import BasePage
from appiumtest2.page.invite_member_page import InviteMemberPage
from appiumtest2.page.search_page import SearchPage


class ContactPage(BasePage):
    _addmemeber_text = "添加成员"
    _search_element = (MobileBy.ID, "com.tencent.wework:id/hxw")

    def goto_invite_member_page(self):
        self.find_by_scroll_and_click(self._addmemeber_text)
        return InviteMemberPage(self.driver)

    def goto_search_page(self):
        self.find_and_click(self._search_element)
        return SearchPage(self.driver)

