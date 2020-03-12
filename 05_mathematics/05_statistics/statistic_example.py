# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 09:10:24
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 09:23:38
from statistics import mean # 平均值
from statistics import mode # 出现最多的数据
from statistics import median # 中位值
from statistics import median_low # 中位低值
from statistics import median_high # 中位高值
from statistics import variance # 方差

data = [1, 2, 2, 5, 10, 12]

print('mean: {:0.2f}'.format(mean(data)))
print('mode: {:0.2f}'.format(mode(data)))
print('median: {:0.2f}'.format(median(data)))
print('median_low: {:0.2f}'.format(median_low(data)))
print('median_high: {:0.2f}'.format(median_high(data)))
print('variance: {:0.2f}'.format(variance(data)))