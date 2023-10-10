#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: fsm.py
@time: 2023/10/10 0:17
@project: programming-pearls-notes
@desc: FSM有穷状态机
"""

trans_out = dict()
trans_out[("LIZ", "0")] = ("LIZ", "0")
trans_out[("LIZ", "1")] = ("LIO", "0")
trans_out[("LIO", "0")] = ("LIZ", "0")
trans_out[("LIO", "1")] = ("LIO", "1")


input_str = "011010111"
state = "LIZ"
for inSym in input_str:
    state, outSym = trans_out[(state, inSym)]
    print(outSym, end="")
