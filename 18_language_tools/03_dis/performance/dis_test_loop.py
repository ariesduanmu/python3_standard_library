# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 11:28:21
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 11:49:12
import sys
import dis
import timeit
import textwrap

module_name = sys.argv[1]
module = __import__(module_name)
Dictionary = module.Dictionary

dis.dis(Dictionary.load_data)
print()

t = timeit.Timer(
    'd = Dictionary(words)',
    textwrap.dedent("""
        from {module_name} import Dictionary
        words = [ 
        l.strip()
        for l in open('text.txt','rt')
        ]
        """).format(module_name=module_name)
    )
iterations = 10
print('TIME: {:0.4f}'.format(t.timeit(iterations) / iterations))
