# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 11:13:51
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 13:18:20
import collections

class Dictionary:
    def __init__(self, words):
        self.by_letter = collections.defaultdict(list)
        self.load_data(words)

    def load_data(self, words):
        by_letter = self.by_letter
        for word in words:
            by_letter[word[0]].append(word)
        
