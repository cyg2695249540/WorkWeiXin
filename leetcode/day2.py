# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day2.py
# @Author   : Pluto.
# @Time     : 2020/11/2 19:02
"""
ex:349
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
说明：
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


def day2(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)


ex = day2(nums1, nums2)
print(ex)
