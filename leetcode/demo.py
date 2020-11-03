# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : demo.py
# @Author   : Pluto.
# @Time     : 2020/11/2 19:15
listA = ['python', '一', '动', '态', '是', '言', '言', '语', '语', '门']


def demo(list):
    resultList  = []
    for i in list:
        if i not in resultList :
            resultList .append(i)
    return resultList

ex=demo(listA)
print(ex)
