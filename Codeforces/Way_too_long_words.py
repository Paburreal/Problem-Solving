#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Way too long words"""
def abbreviation(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[len(word) - 1]
    return word
n =int(input())
for i in range (0, n):
    word = input()
    print(abbreviation(word))
