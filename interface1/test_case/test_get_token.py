# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token.py
# @Author   : Pluto.
# @Time     : 2020/10/29 14:32
import pytest
import yaml

from interface1.api.base_api import BaseApi


def get_datas():
    info = yaml.safe_load(open("../datas/datas.yaml", encoding="utf-8"))
    case = info["demo"]
    ids = info["ids"]
    return case, ids


class TestGetToken:
    def setup(self):
        self.get_token = BaseApi()

    @pytest.mark.parametrize("corpid,corpsecret,errmsg", get_datas()[0], ids=get_datas()[1])
    def test_get_token(self, corpid, corpsecret, errmsg):
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": get_token_url
        }
        r = self.get_token.send_and_requests(req)
        print(r.json()["errmsg"])
        assert r.json()["errmsg"] == errmsg
