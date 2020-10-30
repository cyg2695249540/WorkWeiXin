# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addmember.py
# @Author   : Pluto.
# @Time     : 2020/10/29 18:09
import allure
import pytest
import yaml

from seleniumtest.page.main_page import MainPage


def getdatas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    add1 = datas["add1"]
    case1 = datas["case1"]
    addfail = datas["addfail"]
    case2 = datas["case1"]
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
    @pytest.mark.parametrize("username, acctid, phone", getdatas()[0], ids=getdatas()[1])
    def test_addmember(self, username, acctid, phone):
        namelist = self.main.goto_addmember_page().addmember(username, acctid,
                                                             phone).save_addmember().get_addmember_list()
        assert username in namelist

    @allure.feature("添加成员失败")
    @pytest.mark.parametrize("username, acctid, phone", getdatas()[2], ids=getdatas()[3])
    def test_addmember_fail(self, username, acctid, phone):
        namelist = self.main.goto_addmember_page().addmember(username, acctid,
                                                             phone).cancel_member().get_addmember_list()
        assert username not in namelist

    @allure.feature("通讯录添加成员")
    @pytest.mark.parametrize("username, acctid, phone", getdatas()[4], ids=getdatas()[5])
    def test_contact_addmember(self, username, acctid, phone):
        namelist = self.main.goto_contact_page().goto_addmember_page().addmember(username, acctid,
                                                                                 phone).save_addmember().get_addmember_list()
        assert username in namelist
