# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : invite_member_detail_page.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:07
from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.base_page import BasePage


class InviteMemberDetailPage(BasePage):
    _name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@class='android.widget.EditText']")
    _gender_elemet = (MobileBy.XPATH, "//*[@text='男']")
    _female_element = (MobileBy.XPATH, "//*[@text='女']")
    _male_element = (MobileBy.XPATH, "//*[@text='男']")
    _phone_element = (MobileBy.XPATH,
                      "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    _save_element = (MobileBy.XPATH, "//*[@text='保存']")
    def addname(self,name):
        self.find_and_send_keys(self._name_element,name)
        return self

    def addgender(self,gender):
        self.find_and_click(self._gender_elemet)
        if gender =="女":
            self.wait_for_clickable(self._female_element)
            self.find_and_click(self._female_element)
        else:
            self.wait_for_clickable(self._male_element)
            self.find_and_click(self._male_element)
        return self

    def addphone(self,phone):
        self.find_and_send_keys(self._phone_element,phone)
        return self

    def click_save(self):
        from appiumtest2.page.invite_member_page import InviteMemberPage
        self.find_and_click(self._save_element)
        return InviteMemberPage(self.driver)
