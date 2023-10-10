#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: prime_P1.py
@time: 2023/10/8 9:10
@project: programming-pearls-notes
@desc: 计算素数，程序P1
"""
from line_profiler import LineProfiler


def prime(n):
    for i in range(2, n):
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
