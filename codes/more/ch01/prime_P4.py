#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: prime_P4.py
@time: 2023/10/8 10:55
@project: programming-pearls-notes
@desc: 计算素数，程序P4
"""

import math

from line_profiler import LineProfiler


def root(n):
    return int(math.sqrt(n))


def prime(n):
    if n % 2 == 0:
        return 0
    if n % 3 == 0:
        return 0
    if n % 5 == 0:
        return 0
    bound = root(n)
    for i in range(7, bound + 1, 2):
        if n % i == 0:
            return 0
    return 1


def main():
    res = []
    n = 1000
    for i in range(2, n + 1):
        if prime(i):
            res.append(i)
    return res


if __name__ == '__main__':
    p = LineProfiler()
    p.add_function(prime)
    p_warp = p(main)
    p_warp()
    p.print_stats()
