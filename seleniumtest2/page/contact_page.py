# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/11/3 15:10
from time import sleep

from selenium.webdriver.common.by import By


from seleniumtest2.page.base_page import BasePage


class ContactPage(BasePage):
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    _checkbox = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
    _delete_butto = (By.CSS_SELECTOR, ".js_delete")
    _determine = (By.CSS_SELECTOR, "[d_ck='submit']")

    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")

    _create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _addepartment = (By.CSS_SELECTOR, ".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR, ".jstree-anchor")

    def get_member_list(self):
        self.wait_for_click(self._member_list)
        eles = self.finds(self._member_list)
        return [name.text for name in eles]

    def get_checkbox(self):
        self.wait_for_click(self._checkbox)
        eles = self.finds(self._checkbox)
        return eles

    def deletemember(self,deletename):
        name_box = (By.XPATH, f"//*[@title='{deletename}']/..//input[@type='checkbox']")
        self.wait_for_click(self._checkbox)
        namelist = self.get_member_list()
        if deletename in namelist:
            self.find_and_click(name_box)
        else:
            print("没有该成员")
        self.find_and_click(self._delete_butto)
        self.find_and_click(self._determine)
        return self

    def goto_addmemberpage(self):
        from seleniumtest2.page.addmember_page import AddmemberPage
        while True:
            self.find_and_click(self._addmember_butto)
            try:
                if self.find(self._cancel_member) is not None:
                    break
            except:
                print("再次点击")
        return AddmemberPage(self.driver)

    def goto_addepartment_page(self):
        from seleniumtest2.page.Addepartment_page import AdDepartmentPage
        self.find_and_click(self._create_dropdown)
        self.find_and_click(self._addepartment)
        return AdDepartmentPage()

    def get_department_list(self):
        sleep(1)
        eles=self.finds(self._jstree_anchor)
        return [name.text for name in eles]

