# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-24 10:02:16
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-24 10:06:30
import timeit
import textwrap

setup_statement = ';'.join([
    "l = [(str(x), x) for x in range(1000)]",
    "d = {}"
    ])
t = timeit.Timer(
    textwrap.dedent(
        """
        for s, i in l:
            d[s] = i
        """
        ),
    setup_statement,
    )
print(t.timeit(number=1))