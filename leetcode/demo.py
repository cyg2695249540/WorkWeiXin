# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : demo.py
# @Author   : Pluto.
# @Time     : 2020/11/2 19:15


class Test:
    listA = ['python', '是', '一', '门', '动', '态', '语', '言', '言', '语']

    def test_demo(self):
        resultList = []
        for i in self.listA:
            if i not in resultList:
                resultList.append(i)
        print(resultList)
