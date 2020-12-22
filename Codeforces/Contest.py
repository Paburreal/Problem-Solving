#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contest"""
def Who_got_more_points(Points1, Points2, Time1, Time2):
    if Score_calculation(a, c) > Score_calculation(b, c):
        return "Misha"
    elif Score_calculation(a, c) < Score_calculation(b, c):
        return "Vasya"
    return "Tie"
def Score_calculation(Points, Time):
    return max(3 * Points / 10, Points - ((Points / 250) * Time))

a, b, c, d = map(int, input().split())
print(Who_got_more_points(a, b, c, d))
