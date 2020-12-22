#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instability"""
def Stabilization(a):
    copy_a = []
    a.sort()
    copy_a = a.copy()
    del a[-1]
    del copy_a[0]
    stab1 = a[-1] - a[0]
    stab2 = copy_a[-1] - copy_a[0]
    if stab1 < stab2:
        return stab1
    return stab2

n = int(input())
a = list(map(int, input().split()))
print(Stabilization(a))