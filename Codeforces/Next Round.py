#!/usr/bin/env python3
"""A next round"""
"""Faster/Better input method"""

def pass_next_round(n, k):
    for i in range (0, n):
        if grades[i] == 0:
            return i
        if i > k - 1 and grades[i] != grades[k - 1]:
            return i
    return n

n, k = map(int,input().split())
grades = list(map(int, input().split()))

print(pass_next_round(n, k))
