# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : personal_information_setting_page.py
# @Author   : Pluto.
# @Time     : 2020/11/4 14:08
from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.base_page import BasePage
from appiumtest2.page.edit_member_page import EditMemberPage


class PersonalInformationSettingPage(BasePage):
    _edit_member_element = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def go_to_edit_member_page(self):
        self.find_and_click(self._edit_member_element)
        return EditMemberPage(self.driver)