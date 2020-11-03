# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addmember.py
# @Author   : Pluto.
# @Time     : 2020/11/3 15:08
import allure
import pytest
import yaml

from seleniumtest2.page.main_page import MainPage


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    add1 = datas["add1"]
    case1 = datas["case1"]
    addfail = datas["addfail"]
    case2 = datas["case2"]
    add2 = datas["add2"]
    case3 = datas["case3"]
    return add1, case1, addfail, case2, add2, case3


@allure.feature("添加成员模块")
class TestAddmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.feature("添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[0], ids=get_datas()[1])
    def test_addmember(self, username, acctid, phone):
        list = self.main.goto_addmemberpage().addmember(username, acctid, phone).save_member().get_member_list()
        assert username in list

    @allure.feature("删除成员")
    @pytest.mark.flaky(reruns=1)
    def test_delete_member(self):
        ele1 = self.main.goto_contactpage().get_checkbox()
        toast = self.main.goto_contactpage().deletemember("qq").get_toast_text()
        assert toast == "删除成功"
        ele2 = self.main.goto_contactpage().get_checkbox()
        assert len(ele2) == len(ele1) - 1

    @allure.feature("添加成员失败")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[2], ids=get_datas()[3])
    def test_addmember_fail(self, username, acctid, phone):
        list = self.main.goto_addmemberpage().addmember(username, acctid, phone).cancel_member().get_member_list()
        assert username not in list

    @allure.feature("通讯录添加成员")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("username, acctid, phone", get_datas()[4], ids=get_datas()[5])
    def test_contact_addmember(self, username, acctid, phone):
        list = self.main.goto_contactpage().goto_addmemberpage().addmember(username, acctid,
                                                                    phone).save_member().get_member_list()
        assert username in list
