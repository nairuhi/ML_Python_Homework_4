#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:36:06 2021

@author: nairuhi
"""


def splitstring(string):
    for i in range(1, len(string)):
        if string[:i] == string[i:i+i]:
            return string[:i]
        
    return string

a = "xyzxyzxyz"
splitstring(a)



def stringPower(s, k):
    if k >= 0:
        return k*s
    else:
        x = splitstring(s)
        if -k*x == s:
            return x
        elif k == -1:
            return s
        else:
            return "undefined"
               
s = input()
k = int(input())
print(stringPower(s, k))
