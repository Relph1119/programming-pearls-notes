#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: test_select.py
@time: 2023/10/10 13:33
@project: programming-pearls-notes
@desc: 3.2 选择算法
"""
import random

random.seed(2023)


def good_select(x, l, u, k):
    if l < u:
        l = l + int((u - l + 1) * random.random())
        m = l
        for i in range(l + 1, u):
            if x[i] < x[l]:
                m += 1
                x[m], x[l] = x[l], x[m]
        x[m], x[l] = x[l], x[m]
        if m < k:
            good_select(x, m + 1, u, k)
        elif m > k:
            good_select(x, l, m - 1, k)


def bad_select(x, k):
    global comps
    l = 0
    u = len(x) - 1
    while l < u:
        print(l + 1, u + 1)
        rand_l = l + int((u - l + 1) * random.random())
        x[l], x[rand_l] = x[rand_l], x[l]
        m = l
        comps = comps + u - l
        for i in range(l + 1, u + 1):
            if x[i] < x[l]:
                m += 1
                x[m], x[i] = x[i], x[m]
        x[m], x[l] = x[l], x[m]
        if m < k:
            l = m + 1
        elif m > k:
            u = m - 1


def select(x, k):
    global comps
    l = 0
    u = len(x) - 1
    while l < u:
        rand_l = l + int((u - l + 1) * random.random())
        x[l], x[rand_l] = x[rand_l], x[l]
        t = x[l]
        m = l
        comps = comps + u - l
        for i in range(l + 1, u + 1):
            if x[i] < t:
                m += 1
                x[m], x[i] = x[i], x[m]
        x[m], x[l] = x[l], x[m]
        if m <= k:
            l = m + 1
        elif m >= k:
            u = m - 1


def main_run(args):
    global n, x, comps
    match args[0]:
        case "fill":
            n = args[1]
            x = [random.random() for _ in range(n)]
        case "n":
            n = args[1]
        case "x":
            x[args[1] - 1] = args[2]
        case "print":
            for i in range(n):
                print("   ", x[i])
        case "sel":
            comps = 0
            k = args[1] - 1
            select(x, args[1] - 1)
            print("  compares:", comps)
            print("  compares/n:", comps / n)
            for i in range(k):
                if x[i] > x[k]:
                    print(i)
            for i in range(k + 1, n):
                if x[i] < x[k]:
                    print(i)


def test1():
    main_run(["fill", 2])
    main_run(["x", 1, 5])
    main_run(["x", 2, 5])
    main_run(["print"])
    main_run(["sel", 2])


def test2():
    main_run(["fill", 50])
    main_run(["sel", 25])
    main_run(["fill", 100])
    main_run(["sel", 50])


if __name__ == '__main__':
    test2()
