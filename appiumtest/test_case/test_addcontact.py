# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addcontact.py
# @Author   : Pluto.
# @Time     : 2020/10/30 19:00
import allure
import pytest
import yaml

from appiumtest.page.app import App


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    add = datas["add"]
    case1 = datas["case1"]
    return add, case1


@allure.feature("添加成员模块")
class TestAddcontact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        self.app.stop()

    @allure.feature("添加成员")
    @pytest.mark.parametrize("name, gender, phone", get_datas()[0], ids=get_datas()[1])
    def test_addcontact(self, name, gender, phone):
        mytost = self.main.goto_contact().addmember().goto_addmember_detail_page().addname(name).addgender(
            gender).addphone(phone).save_member().get_toast()
        assert mytost == "添加成功"
