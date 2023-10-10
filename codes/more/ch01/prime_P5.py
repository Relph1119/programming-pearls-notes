#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: prime_P5.py
@time: 2023/10/8 11:02
@project: programming-pearls-notes
@desc: 计算素数，程序P4
"""

from line_profiler import LineProfiler


def prime(n):
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    i = 7
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 2

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
