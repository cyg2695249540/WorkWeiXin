# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_deletemember.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:51
import allure
import pytest
from appium.webdriver.common.mobileby import MobileBy

from appiumtest2.page.app import App


@allure.feature("删除成员模块")
class TestDeletemember:
    def setup(self):
        self.app = App()
        self.main = self.app.startapp().goto_main_page()

    def teardown(self):
        self.app.stopapp()

    @allure.feature("正确删除成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name", [("LCQ")], ids={"正确删除成员"})
    def test_deletemember(self, name):
        result = self.main.goto_contact_page().goto_search_page().searchmember(
            name).go_to_personal_information_setup_page().go_to_edit_member_page().delete_member().search_result()
        assert result == "无搜索结果"
