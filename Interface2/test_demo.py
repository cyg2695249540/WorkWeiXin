# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/11/2 12:40
import requests
from jsonpath import jsonpath


class TestDemo:
    def setup_class(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=get_token_url)
        self.token = r.json()["access_token"]
        return self.token

    def test_create_department(self):
        create_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 3,
            "id": 4
        }
        r = requests.post(url=create_department_url, json=data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.get(url=get_department_list_url)
        assert r.status_code == 200
        list = r.json()
        departmentname = jsonpath(list, "$..department[?(@.id==4)].name")[0]
        assert "技术部" == departmentname

    def test_update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": 4,
            "name": "测试研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, json=data)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "updated"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.get(url=get_department_list_url)
        assert r.status_code == 200
        list = r.json()
        departmentname = jsonpath(list, "$..department[?(@.id==4)].name")[0]
        assert "测试研发中心" == departmentname

    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=4"
        r = requests.get(url=delete_url)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "deleted"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.get(url=get_department_list_url)
        assert r.status_code == 200
        list = r.json()
        departmentids = jsonpath(list, "$..id")
        assert 4 not in departmentids
