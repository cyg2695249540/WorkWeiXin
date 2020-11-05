# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_case.py
# @Author   : Pluto.
# @Time     : 2020/11/4 15:59
from typing import List


class TestCase:
    _intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    _newInterval = [4, 8]

    def test_case(self):
        left, right = self._newInterval
        placed = False
        ans = list()
        for li, ri in self._intervals:
            if ri < left:
                ans.append([li, ri])
            elif li > right:
                ans.append([li, ri])
                ans.append([left, right])
                placed = True
            else:
                left = min(li, left)
                right = max(ri, right)
        if not placed:
            ans.append([left, right])
        print(ans)
