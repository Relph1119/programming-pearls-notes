#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: test_bsearch.py
@time: 2023/10/10 11:10
@project: programming-pearls-notes
@desc: 3.1 二分搜索
"""


def bsearch(x, t):
    n = len(x[1:])
    l = 1
    u = n
    while l <= u:
        m = (l + u) // 2
        print("   ", l, m, u)
        if x[m] < t:
            l = m + 1
        elif x[m] > t:
            # 该段代码有问题
            u = m - 1
        else:
            return m
    return 0


def main_run(args):
    global n, x
    match args[0]:
        case "fill":
            n = args[1]
            x = [10 * i for i in range(n + 1)]
        case "n":
            n = args[1]
        case "x":
            x[args[1]] = args[2]
        case "print":
            for i in range(1, n + 1):
                print(i, ":\t", x[i])
        case "search":
            t = bsearch(x, args[1])
            print("result:", t)


if __name__ == '__main__':
    main_run(["fill", 5])
    main_run(["print"])
    main_run(["search", 10])
    main_run(["search", 40])
    main_run(["search", 30])
    main_run(["search", 50])
