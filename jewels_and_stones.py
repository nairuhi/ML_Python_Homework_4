#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:54:41 2021

@author: nairuhi
"""


def numJewelsInStones(jewels, stones):
    s = 0
    for i in jewels:
        s += stones.count(i)
    return s



jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

jewels = "z"
stones = "ZZ"
print(numJewelsInStones(jewels, stones))

