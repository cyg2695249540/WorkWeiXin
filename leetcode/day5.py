# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : day5.py
# @Author   : Pluto.
# @Time     : 2020/11/5 12:17
"""
ex:127
给定两个单词（beginWord和 endWord）和一个字典，找到从beginWord 到endWord 的最短转换序列的长度。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出:0
解释:endWord "cog" 不在字典中，所以无法进行转换。
"""
from typing import List
class Test:
    _beginWord = "hit",
    _endWord = "cog",
    _wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    def test_ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if self._endWord not in self._wordList:
            print(0)
        else:
            pass


