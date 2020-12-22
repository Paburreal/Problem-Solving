#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Mislove has lost an array """



def sum_of_table_of_2(index):
    table = [1]
    for i in range(index - 1):
       table.append(2 * table[i])
    return table
def max_min_sum(number_of_elements, not_less_than, not_more_than):
    Minimum = number_of_elements - not_less_than + sum(sum_of_table_of_2(not_less_than))
    Maximum = (number_of_elements - not_more_than) * sum_of_table_of_2(not_more_than)[-1] + sum(sum_of_table_of_2(not_more_than))
    return str(Minimum) +  " " + str(Maximum)

n, l, r = map(int, input().split())
print(max_min_sum(n, l, r))