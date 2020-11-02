# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2020/11/2 13:33
from Interface2.api.baseApi import BaseApi


class WeWork(BaseApi):
    def get_token(self,corpsecret):
        corpid = "ww0ae123b953d2b956"
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "post",
            "url": get_token_url,
        }
        r=self.send_and_requests(req)
        self.token=r.json()["access_token"]
        return self.token
