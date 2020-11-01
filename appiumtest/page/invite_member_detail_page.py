# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : invite_member_detail_page.py
# @Author   : Pluto.
# @Time     : 2020/10/30 17:00
from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage


class InviteMemberDetailPage(BasePage):
    _name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@class='android.widget.EditText']")
    _gender_elemet = (MobileBy.XPATH, "//*[@text='男']")
    _female_element = (MobileBy.XPATH, "//*[@text='女']")
    _male_element = (MobileBy.XPATH, "//*[@text='男']")
    _phone_element = (MobileBy.XPATH,"//*[@text='手机号']")
    _save_element = (MobileBy.XPATH, "//*[@text='保存']")
    def addname(self,name):
        self.find_and_send_keys(self._name_element,name)
        return self

    def addgender(self,gender):
        self.find_and_click(self._gender_elemet)
        if gender == "女":
            self.wait_for_click(self._female_element)
            self.find_and_click(self._female_element)
        else:
            self.wait_for_click(self._male_element)
            self.find_and_click(self._male_element)
        return self

    def addphone(self,phone):
        self.find_and_send_keys(self._phone_element,phone)
        return self

    def save_member(self):
        from appiumtest.page.invite_member_page import InviteMemberPage
        self.find_and_click(self._save_element)
        return InviteMemberPage(self.driver)
