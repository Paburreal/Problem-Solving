#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grow the tree"""
def largest_polyline(number_of_sticks, sticks_lengths):
    sticks_lengths.sort()
    lower_half = sticks_lengths[:len(sticks_lengths) // 2]
    bigger_half = sticks_lengths[len(sticks_lengths) // 2 :]
    return sum(bigger_half) ** 2 + sum(lower_half) ** 2



n = map(int, input())
a = list(map(int, input().split()))
print(largest_polyline(n, a))
