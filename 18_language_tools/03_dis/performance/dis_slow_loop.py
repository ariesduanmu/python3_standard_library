# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 11:13:26
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 11:58:42
class Dictionary:
    def __init__(self, words):
        self.by_letter = {}
        self.load_data(words)

    def load_data(self, words):
        for word in words:
            try:
                self.by_letter[word[0]].append(word)
            except KeyError:
                self.by_letter[word[0]] = [word]