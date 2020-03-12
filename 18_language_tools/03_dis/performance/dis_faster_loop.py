# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 11:13:40
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 11:58:40
import string


class Dictionary:
    def __init__(self, words):
        self.by_letter = {
        letter : []
        for letter in string.ascii_letters
        }
        self.load_data(words)

    def load_data(self, words):
        for word in words:
            self.by_letter[word[0]].append(word)

