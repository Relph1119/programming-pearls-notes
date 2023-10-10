#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: select.py
@time: 2023/10/10 19:59
@project: programming-pearls-notes
@desc: 15.2 选择算法
"""

import random

random.seed(2023)


def select(x, k):
    l = 0
    u = len(x)
    while l < u:
        rand = random.randint(l, u)
        x[l], x[rand] = x[rand], x[l]
        m = l
        for i in range(l + 1, u):
            if x[i] < x[l]:
                m += 1
                x[m], x[i] = x[i], x[m]
        x[m], x[l] = x[l], x[m]
        if k <= m:
            u = m - 1
        elif k >= m:
            l = m + 1


if __name__ == '__main__':
    x = [random.random() for _ in range(5)]
    k = 3
    select(x, k - 1)
    print("x: ", x)
    print(f"x{k - 1}: {x[k -1]}")
