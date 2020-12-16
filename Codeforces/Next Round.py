#!/usr/bin/env python3
"""A next round"""
n = int(input())
k = int(input())

def pass_next_round(n, k):
    grades = []
    for i in range (0, n):
        grades.append(int(input()))
        if grades[i] == 0:
            return i
        if i > k - 1 and grades[i] != grades[k - 1]:
            return i
    return n

print(pass_next_round(n, k))
