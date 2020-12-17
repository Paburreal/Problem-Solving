#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Football"""
def is_dangerous(players_formation):
    previous_player, dangerous_meter = 2, 0
    for player in players_formation: 
        if player == previous_player:
            dangerous_meter += 1
        else:
            dangerous_meter = 0
        if dangerous_meter == 6:
            return "YES"
        previous_player = player
    return "NO"

players_formation = list(map(int, input()))

print(is_dangerous(players_formation))