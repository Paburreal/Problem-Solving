#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Death Note"""
def pages_turned(names_capacity, number_of_names):
    temp = 0
    pages = []
    for number in number_of_names:
        number += temp
        pages.append(number // names_capacity)
        if number // names_capacity > 0:  
            temp = number % names_capacity
        else:
            temp = number
    return pages

n, m = map(int, input().split())
a = list(map(int, input().split()))

print( " ".join(map(str, pages_turned(m, a))))
        
