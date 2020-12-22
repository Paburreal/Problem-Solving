#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Equalize Price """
def Equalized_Price(n, k, old_prices):
    old_prices.sort()
    if old_prices[0] + k >= old_prices[-1] - k:
        return old_prices[0] + k
    return -1

q = int(input())

for querie in range (0, q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print (Equalized_Price(n, k, a))
    