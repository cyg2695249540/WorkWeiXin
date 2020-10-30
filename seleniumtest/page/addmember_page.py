# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addmember_page.py
# @Author   : Pluto.
# @Time     : 2020/10/29 18:11
from selenium.webdriver.common.by import By

from seleniumtest.page.base_page import BasePage
from seleniumtest.page.contact_page import ContactPage


class AddmemberPage(BasePage):
    _username = (By.CSS_SELECTOR, "[id='username']")
    _acctid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _phone = (By.CSS_SELECTOR, "[id='memberAdd_phone']")
    _save_member = (By.CSS_SELECTOR, ".js_btn_save")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave = (By.CSS_SELECTOR, "[node-type='cancel']")

    def addmember(self, username, acctid, phone):
        self.find_and_send_keys(self._username, username)
        self.find_and_send_keys(self._acctid, acctid)
        self.find_and_send_keys(self._phone, phone)
        return self

    def save_addmember(self):
        self.find_and_click(self._save_member)
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find_and_click(self._cancel_member)
        self.find_and_click(self._leave)
        return ContactPage(self.driver)
