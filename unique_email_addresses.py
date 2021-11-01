#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 13:15:21 2021

@author: nairuhi
"""


def numUniqueEmails(emails):
        unique = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            unique.add(f'{local}@{domain}')
        return len(unique)
    

emails = [i for i in input().split(' ')]

print(numUniqueEmails(emails))


