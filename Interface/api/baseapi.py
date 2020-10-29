# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : baseapi.py
# @Author   : Pluto.
# @Time     : 2020/10/28 19:18
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BasePage:
    def send_requests(self, req: dict):
        return requests.request(**req)

    def base_jsonpath(self, obj, expr):
        return jsonpath(obj, expr)

    def base_jsonschema(self, instance, schema):
        return validate(instance, schema)
