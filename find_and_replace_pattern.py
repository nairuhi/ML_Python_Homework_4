#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:38:55 2021

@author: nairuhi
"""

def findAndReplacePattern(words, pattern):   
        output = []
        for word in words:
            distinct_mappings = set(list(zip(word, pattern)))
            
            n = len(distinct_mappings)
            
            lefts  = len(set([a for a, b in distinct_mappings]))
            rights = len(set([b for a, b in distinct_mappings]))
            
            if lefts == n and rights == n:
                output.append(word)

        return output



words = [i for i in input().split()]
pattern = input()

print(findAndReplacePattern(words, pattern))

