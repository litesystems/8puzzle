#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from copy import deepcopy


class Puzzle(object):
    def __init__(self, table):
        if not self._validate(table):
            raise ValueError()
        self.table = deepcopy(table)
        self.width = len(self.table[0])
        self.height = len(self.table)
        self.fs = 0
        self.gs = 0
        self.hs = 0
        self.n = []
        self.parent = None

    def next_puzzles(self):
        """パズルの現状態から1段階移動したパスルのリストを返す"""
        puzzles = []

        # 空いているセルの場所を探す
        zero_x, zero_y = -1, -1
        for y, row in enumerate(self.table):
            for x, cell in enumerate(row):
                if cell == 0:
                    zero_x = x
                    zero_y = y

        # Up
        if zero_y > 0:
            table = deepcopy(self.table)
            table[zero_y][zero_x], table[zero_y - 1][zero_x] = \
                table[zero_y - 1][zero_x], table[zero_y][zero_x]
            puzzles.append(Puzzle(table))

        # Down
        if zero_y < (self.height - 1):
            table = deepcopy(self.table)
            table[zero_y][zero_x], table[zero_y + 1][zero_x] = \
                table[zero_y + 1][zero_x], table[zero_y][zero_x]
            puzzles.append(Puzzle(table))

        # Left
        if zero_x > 0:
            table = deepcopy(self.table)
            table[zero_y][zero_x], table[zero_y][zero_x - 1] = \
                table[zero_y][zero_x - 1], table[zero_y][zero_x]
            puzzles.append(Puzzle(table))

        # Right
        if zero_x < (self.width - 1):
            table = deepcopy(self.table)
            table[zero_y][zero_x], table[zero_y][zero_x + 1] = \
                table[zero_y][zero_x + 1], table[zero_y][zero_x]
            puzzles.append(Puzzle(table))

        return puzzles

    def is_answer(self):
        answer_table = []
        for i in range(1, self.width * self.height, self.width):
            answer_table.append(list(range(i, i + self.width)))
        answer_table[-1][-1] = 0
        for row_p, row_a in zip(self.table, answer_table):
            for cell_p, cell_a in zip(row_p, row_a):
                if cell_p != cell_a:
                    return False
        return True

    def _validate(self, table):
        m = None
        for n in map(len, table):
            if m is None:
                m = n
            if n != m:
                return False
        return True

    def __eq__(self, puzzle):
        for row_a, row_b in zip(self.table, puzzle.table):
            for cell_a, cell_b in zip(row_a, row_b):
                if cell_a != cell_b:
                    return False
        return True

    def __ne__(self, puzzle):
        return not self.__eq__(puzzle)

    def __str__(self):
        rows = []
        for row in self.table:
            rows.append(' '.join(map(str, row)))
        return '\n'.join(rows)

    def __repr__(self):
        return ("n=%s, f=%d, g=%d, h=%d, tb=%s" % (
            str(self.n), self.fs, self.gs, self.hs, str(self.table)))
