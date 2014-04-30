#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

from eight import heuristic
from eight.puzzle import Puzzle


class TestHeuristicFunctions(unittest.TestCase):
    def test_diff(self):
        h = heuristic.diff(Puzzle([[2, 3, 1], [5, 4, 6], [7, 0, 8]]))
        self.assertEqual(h, 6)

    def test_manhattan(self):
        h = heuristic.manhattan(Puzzle([[2, 1, 3], [4, 5, 6], [7, 0, 8]]))
        self.assertEqual(h, 3)
