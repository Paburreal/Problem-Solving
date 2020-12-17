#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Decoding - 900 """
def Decode_Sveta(lenght_of_string, string):
    codified_word = list(string)
    decodified_word = []
    decodified_word.append(codified_word.pop(-1))
    while len(codified_word) != 0:
        decodified_word.insert(len(decodified_word) // 2, codified_word.pop(-1))
    return "".join(decodified_word)
            
n = map(int, input().split())
s = input()
print(Decode_Sveta(n, s))
