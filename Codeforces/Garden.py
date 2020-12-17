#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Garden"""
def best_bucket(number_of_buckets, lenght_of_garden, buckets):
    buckets.sort(reverse = True)
    for bucket in buckets:
        if lenght_of_garden % bucket == 0:
            return lenght_of_garden // bucket

n, k = map(int, input().split())
a = list(map(int, input().split()))

print (best_bucket(n, k, a))