# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2020/10/28 19:15
import json

import allure
import pytest
import yaml

from Interface.api.department import Department


@allure.feature("部门模块")
class TestDepartmrnt:
    def setup(self):
        self.department = Department()
        corpsecret_info = yaml.safe_load(open("config.yaml", encoding="utf-8"))
        corpsecret_department = corpsecret_info["token"]["department_secret"]
        self.department.get_token(corpsecret_department)

    @allure.feature("添加部门")
    @pytest.mark.parametrize("department_id, department_name", [(4, "技术部")], ids={"添加部门"})
    def test_create_department(self, department_id, department_name):
        r = self.department.create_department(department_id, department_name)
        assert r["errcode"] == 0 and r["errmsg"] == "created"
        list = self.department.get_department_list()
        name = self.department.base_jsonpath(list, f"$..department[?(@.id=={department_id})].name")[0]
        assert department_name == name

    @allure.feature("更新部门")
    @pytest.mark.parametrize("department_id, department_name", [(4, "测试研发中心")], ids={"更新部门"})
    def test_update_department(self, department_id, department_name):
        r = self.department.update_department(department_id, department_name)
        assert r["errcode"] == 0 and r["errmsg"] == "updated"
        list = self.department.get_department_list()
        name = self.department.base_jsonpath(list, f"$..department[?(@.id=={department_id})].name")[0]
        assert department_name == name

    @allure.feature("删除部门")
    @pytest.mark.parametrize("department_id", [(4)], ids={"删除部门"})
    def test_delete_department(self, department_id):
        r = self.department.delete_department(department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "deleted"
        list = self.department.get_department_list()
        ids = self.department.base_jsonpath(list, "$..id")
        assert department_id not in ids

    @allure.feature("字段格式验证")
    def test_get_department_list(self):
        list = self.department.get_department_list()
        get_department_list = json.load(open("./json_schema/get_list_schema.json", encoding="utf-8"))
        self.department.base_jsonschema(list, get_department_list)
