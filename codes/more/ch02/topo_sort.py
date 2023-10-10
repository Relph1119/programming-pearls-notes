#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: topo_sort.py
@time: 2023/10/10 0:25
@project: programming-pearls-notes
@desc: 拓扑排序
"""
from collections import defaultdict

topos = [["A", "B"],
         ["A", "F"],
         ["B", "F"],
         ["E", "B"],
         ["I", "E"],
         ["G", "E"],
         ["E", "D"],
         ["F", "H"],
         ["D", "H"],
         ["G", "C"],
         ["I", "C"]]

predct = defaultdict(int)
succcnt = defaultdict(int)
succlist = dict()
for topo in topos:
    predct[topo[1]] += 1
    if topo[0] not in predct.keys():
        predct[topo[0]] = 0
    succcnt[topo[0]] += 1
    succlist[(topo[0], succcnt[topo[0]])] = topo[1]

qlo = 1
n = 0
q = []
for i in predct.keys():
    n += 1
    if predct[i] == 0:
        q.append(i)
qhi = len(q)

result = []

while qlo <= qhi:
    t = q[qlo - 1]
    result.append(t)
    qlo += 1
    for i in range(1, succcnt[t] + 1):
        s = succlist[(t, i)]
        predct[s] -= 1
        if predct[s] == 0:
            q.append(s)
            qhi += 1

print("->".join(result))

if qhi != n:
    print("tsort error: cycle in input")
