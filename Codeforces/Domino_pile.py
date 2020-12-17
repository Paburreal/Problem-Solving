#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Domino pile """
M, N = map(int, input().split())

def max_dominos(base, height):
    if base % 2 != 0 and height % 2 != 0:
        return ((base * height + 1) / 2) - 1
    return base * height / 2

print(int(max_dominos(M, N)))
