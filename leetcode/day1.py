# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day1.py
# @Author   : Pluto.
# @Time     : 2020/11/1 15:50
"""
ex:1
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from typing import List


class Test:
    _nums = [2, 7, 11, 15]
    _target = 9

    def test_addnums(self):
        dic = {}
        for k, v in enumerate(self._nums):
            if self._target - v in dic:
                print([dic[self._target - v], k])
            dic[v] = k

