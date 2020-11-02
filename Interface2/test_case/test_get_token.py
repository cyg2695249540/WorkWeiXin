# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token.py
# @Author   : Pluto.
# @Time     : 2020/11/2 13:05
import allure
import pytest
import yaml

from Interface2.api.baseApi import BaseApi


def get_datas():
    datas = yaml.safe_load(open("../datas/datas.yaml", encoding="utf-8"))
    demo = datas["demo"]
    case = datas["case"]
    return demo, case


@allure.feature("获取get_token模块")
class TestGetToken:
    def setup(self):
        self.token = BaseApi()

    @allure.feature("get_token测试")
    @pytest.mark.parametrize("corpid,corpsecret,errmsg", get_datas()[0], ids=get_datas()[1])
    def test_get_token(self, corpid, corpsecret, errmsg):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": get_token_url
        }
        r = self.token.send_and_requests(req)
        assert r.status_code == 200
        assert r.json()["errmsg"] == errmsg
