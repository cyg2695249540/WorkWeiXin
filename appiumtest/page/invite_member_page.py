# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : invite_member_page.py
# @Author   : Pluto.
# @Time     : 2020/10/30 16:59
from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage
from appiumtest.page.invite_member_detail_page import InviteMemberDetailPage


class InviteMemberPage(BasePage):
    _addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def goto_addmember_detail_page(self):
        self.find_and_click(self._addmember_element)
        return InviteMemberDetailPage(self.driver)

    def get_toast(self):
        return self.get_toast_text()
