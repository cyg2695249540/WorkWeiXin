# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/10/29 13:50
import json

import allure
import pytest
import yaml

from interface1.api.department import Department


@allure.feature("部门模块")
class TestDepartment:
    def setup(self):
        self.department = Department()
        token_info = yaml.safe_load(open("config.yaml", encoding="utf-8"))
        department_secret = token_info["token"]["department_secret"]
        self.department.get_token(department_secret)

    @allure.feature("添加部门")
    @pytest.mark.parametrize("department_name,department_id", [("技术部", 4)], ids={"添加部门"})
    def test_create_department(self, department_name, department_id):
        r = self.department.create_department(department_name, department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "created"
        list = self.department.get_departmemt_list()
        name = self.department.base_jsonpath(list, f"$..department[?(@.id=={department_id})].name")[0]
        assert department_name == name

    @allure.feature("更新部门")
    @pytest.mark.parametrize("department_name,department_id", [("测试研发中心", 4)], ids={"更新部门"})
    def test_update_department(self, department_name, department_id):
        r = self.department.update_department(department_name, department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "updated"
        self.department.get_departmemt_list()
        list = self.department.get_departmemt_list()
        name = self.department.base_jsonpath(list, f"$..department[?(@.id=={department_id})].name")[0]
        assert department_name == name

    @allure.feature("删除部门")
    @pytest.mark.parametrize("department_id", [(4)], ids={"删除部门"})
    def test_delete_department(self, department_id):
        r = self.department.delete_department(department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "deleted"
        list = self.department.get_departmemt_list()
        departmentids = self.department.base_jsonpath(list, "$..id")
        assert department_id not in departmentids

    @allure.feature("字段校验")
    def test_get_department_list(self):
        list = self.department.get_departmemt_list()
        get_department_list = json.load(open("./json_schema/get_list_schema.json", encoding="utf-8"))
        self.department.base_jsonschema(list, get_department_list)
