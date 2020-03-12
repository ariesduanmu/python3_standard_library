# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 11:14:06
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 11:28:10
import operator
import itertools

class Dictionary:
    def __init__(self, words):
        self.by_letter = {}
        self.load_data(words)

    def load_data(self, words):
        groups = itertools.groupby(
            words,
            key=operator.itemgetter(0),
            )
        self.by_letter = {group[0]:group[1] for group in groups}