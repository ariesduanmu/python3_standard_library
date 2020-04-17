# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 14:55:50
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 15:45:59
# 10.4.18 Implementing MapReduce

import collections
import itertools
import multiprocessing

class SimpleMapReduce:
    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func =  reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(
            self.map_func,
            inputs,
            chunksize=chunksize
            )
        partitioned_data = self.partition(
            itertools.chain(*map_responses)
            )
        reduced_values = self.pool.map(
            self.reduce_func,
            partitioned_data,
            )
        return reduced_values
