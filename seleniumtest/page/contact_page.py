# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/10/29 18:11
from time import sleep

from selenium.webdriver.common.by import By


from seleniumtest.page.base_page import BasePage


class ContactPage(BasePage):
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")

    _checkbox = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
    _delete_butto = (By.CSS_SELECTOR, ".js_delete")
    _determine = (By.CSS_SELECTOR, "[d_ck='submit']")

    _create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _adddepartment = (By.CSS_SELECTOR, ".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR, ".jstree-anchor")

    def goto_addmember_page(self):
        from seleniumtest.page.addmember_page import AddmemberPage
        while True:
            self.find_and_click(self._addmember_butto)
            try:
                if self.find(self._cancel_member) is not None:
                    break
            except:
                print("再次点击")
        return AddmemberPage(self.driver)

    def get_addmember_list(self):
        self.wait_for_click(self._member_list)
        eles = self.finds(self._member_list)
        return [name.text for name in eles]

    def delete_member(self):
        self.wait_for_click(self._checkbox)
        checkboxs = self.finds(self._checkbox)
        if checkboxs is not None:
            checkboxs[0].click()
        else:
            print("没有其他成员")
        self.find_and_click(self._delete_butto)
        self.find_and_click(self._determine)
        return self

    def get_toast(self):
        toast = self.get_toast_text()
        return toast

    def go_to_adddepartment_page(self):
        from seleniumtest.page.addpartment_page import AddpartmentPage
        self.find_and_click(self._create_dropdown)
        self.find_and_click(self._adddepartment)
        return AddpartmentPage()

    def get_department_list(self):
        sleep(1)
        eles=self.finds(self._jstree_anchor)
        return [name.text for name in eles]