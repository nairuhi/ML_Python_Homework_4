#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:12:20 2021

@author: nairuhi
"""


def findingUsersActiveMinutes(logs, k):
    d = {}
    for i in logs:
        if not d.get(i[0]):
            d.update({i[0]:[i[1]]})
        else:
            d[i[0]].append(i[1])
    
    l = [0 for i in range(1, k+1)]
    for i in d.values():
        l[len(set(i))-1]+=1
    return l

    

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(findingUsersActiveMinutes(logs, k))

logs = [[1,1],[2,2],[2,3]]
k = 4
print(findingUsersActiveMinutes(logs, k))

