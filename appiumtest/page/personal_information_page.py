# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : personal_information_page.py
# @Author   : Pluto.
# @Time     : 2020/11/1 14:45
from appium.webdriver.common.mobileby import MobileBy

from appiumtest.page.base_page import BasePage
from appiumtest.page.personal_information_setting_page import PersonalInformationSettingPage


class PersonalInformationPage(BasePage):
    _edit_element = (MobileBy.ID, "hxm")
    def go_to_personal_information_setup_page(self):
        self.find_and_click(self._edit_element)
        return PersonalInformationSettingPage(self.driver)