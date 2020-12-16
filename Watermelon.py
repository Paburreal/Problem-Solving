#!/usr/bin/env python3
"""Watermelon"""
def split_is_even(num_watermelons):
    if num_watermelons % 2 == 0 and num_watermelons != 2:
        return "YES"
    return "NO"

w = int(input())
print(split_is_even(w))
