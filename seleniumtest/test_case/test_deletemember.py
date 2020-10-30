# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_deletemember.py
# @Author   : Pluto.
# @Time     : 2020/10/29 19:35
import allure

from seleniumtest.page.main_page import MainPage


@allure.feature("删除成员模块")
class TestDeletemember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.feature("删除成员")
    def test_deletement(self):
        toast = self.main.goto_contact_page().delete_member().get_toast()
        assert toast == "删除成功"
