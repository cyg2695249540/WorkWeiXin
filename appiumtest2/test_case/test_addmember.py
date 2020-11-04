# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addmember.py
# @Author   : Pluto.
# @Time     : 2020/11/4 13:08
import allure
import pytest
import yaml

from appiumtest2.page.app import App


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    add = datas["add"]
    case1 = datas["case1"]
    return add, case1


@allure.feature("添加成员模块")
class TestAddmember:
    def setup(self):
        self.app = App()
        self.main = self.app.startapp().goto_main_page()

    def teardown(self):
        self.app.stopapp()

    @allure.feature("正确添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("name, gender, phone", get_datas()[0], ids=get_datas()[1])
    def test_addmember(self, name, gender, phone):
        toast_text = self.main.goto_contact_page().goto_invite_member_page().goto_invite_member_detail_page().addname(
            name).addgender(gender).addphone(phone).click_save().get_toast_text()
        assert toast_text == "添加成功"
