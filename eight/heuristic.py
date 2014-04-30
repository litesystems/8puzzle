#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def diff(puzzle):
    """推定関数 (位置が正しくないタイルの数)"""
    value = 0
    for row_p, row_a in zip(puzzle.table, _answer_table(puzzle)):
        for cell_p, cell_a in zip(row_p, row_a):
            if cell_p == 0:
                continue
            if cell_p != cell_a:
                value += 1
    return value


def manhattan(puzzle):
    """推定関数 (マンハッタン距離)"""
    value = 0

    p_x, p_y = -1, -1
    for i in range(1, puzzle.width * puzzle.height):
        a_x = (i - 1) % puzzle.width
        a_y = (i - 1) // puzzle.width
        for y, row_p in enumerate(puzzle.table):
            for x, cell in enumerate(row_p):
                if cell == i:
                    p_x, p_y = x, y
        value += abs(p_y - a_y)
        value += abs(p_x - a_x)
    return value


def _answer_table(puzzle):
    """パズルの答えのリストを作成する処理"""
    answer_table = []
    for i in range(1, puzzle.width * puzzle.height, puzzle.width):
        answer_table.append(list(range(i, i + puzzle.width)))
    answer_table[-1][-1] = 0
    return answer_table
