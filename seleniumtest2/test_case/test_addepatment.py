# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addepatment.py
# @Author   : Pluto.
# @Time     : 2020/11/3 15:12
import allure
import pytest
import yaml

from seleniumtest2.page.main_page import MainPage


def get_datas():
    datas = yaml.safe_load(open("../datas/addcontact.yml", encoding="utf-8"))
    addepartment = datas["addepartment"]
    case1 = datas["case4"]
    addepartmentfail = datas["addepartmentfail"]
    case2 = datas["case5"]
    return addepartment, case1, addepartmentfail, case2


@allure.feature("添加部门")
class TestAddepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.feature("添加部门成功")
    @pytest.mark.parametrize("departmentname", get_datas()[0], ids=get_datas()[1])
    def test_addepartment(self, departmentname):
        departmentnamelist = self.main.goto_contactpage().goto_addepartment_page().addepartment(
            departmentname).save_department().get_department_list()
        assert departmentname in departmentnamelist

    @allure.feature("添加部门失败")
    @pytest.mark.parametrize("departmentname", get_datas()[2], ids=get_datas()[3])
    def test_addepartment_cancel(self, departmentname):
        departmentnamelist = self.main.goto_contactpage().goto_addepartment_page().addepartment(
            departmentname).cancel_department().get_department_list()
        assert departmentname not in departmentnamelist
