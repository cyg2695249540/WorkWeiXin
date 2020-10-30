# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addpartment.py
# @Author   : Pluto.
# @Time     : 2020/10/29 20:22
import allure
import pytest
import yaml

from seleniumtest.page.main_page import MainPage


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    adddepartment = datas["adddepartment"]
    case1 = datas["case4"]
    adddepartmentfail = datas["adddepartmentfail"]
    case2 = datas["case5"]
    return adddepartment, case1, adddepartmentfail, case2


@allure.feature("添加部门模块")
class TestAddpartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.feature("确认添加部门")
    @pytest.mark.parametrize("departmentname", get_datas()[0], ids=get_datas()[1])
    def test_adddepartment(self, departmentname):
        departmentlist = self.main.goto_contact_page().go_to_adddepartment_page().adddepartment(
            departmentname).save_department().get_department_list()
        assert departmentname in departmentlist

    @allure.feature("添加部门失败")
    @pytest.mark.parametrize("departmentname", get_datas()[2], ids=get_datas()[3])
    def test_adddepartment_cancel(self, departmentname):
        departmentlist = self.main.goto_contact_page().go_to_adddepartment_page().adddepartment(
            departmentname).cancel_department().get_department_list()
        assert departmentname not in departmentlist
