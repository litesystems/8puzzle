#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

from eight.puzzle import Puzzle


class TestPuzzle(unittest.TestCase):
    def test_str(self):
        puzzle = [[2, 3, 1], [5, 4, 6], [0, 8, 7]]
        expected = "2 3 1\n5 4 6\n0 8 7"
        ep = Puzzle(puzzle)
        self.assertEqual(str(ep), expected)

    def test_eq(self):
        ep1 = Puzzle([[2, 3, 1], [5, 4, 6], [0, 8, 7]])
        ep2 = Puzzle([[2, 3, 1], [5, 4, 6], [0, 8, 7]])
        ep3 = Puzzle([[1, 3, 2], [5, 4, 6], [0, 8, 7]])
        self.assertTrue(ep1 == ep2)
        self.assertFalse(ep1 == ep3)

    def test_ne(self):
        ep1 = Puzzle([[2, 3, 1], [5, 4, 6], [0, 8, 7]])
        ep2 = Puzzle([[2, 3, 1], [5, 4, 6], [0, 8, 7]])
        ep3 = Puzzle([[1, 3, 2], [5, 4, 6], [0, 8, 7]])
        self.assertFalse(ep1 != ep2)
        self.assertTrue(ep1 != ep3)

    def test_next_puzzles(self):
        ep0 = Puzzle([[2, 3, 1], [5, 4, 6], [0, 8, 7]])
        ep1 = Puzzle([[2, 3, 1], [0, 4, 6], [5, 8, 7]])
        ep2 = Puzzle([[2, 3, 1], [5, 4, 6], [8, 0, 7]])
        self.assertEqual(ep0.next_puzzles(), [ep1, ep2])

        ep3 = Puzzle([[2, 0, 1], [5, 4, 6], [3, 8, 7]])
        ep4 = Puzzle([[2, 4, 1], [5, 0, 6], [3, 8, 7]])
        ep5 = Puzzle([[0, 2, 1], [5, 4, 6], [3, 8, 7]])
        ep6 = Puzzle([[2, 1, 0], [5, 4, 6], [3, 8, 7]])
        self.assertEqual(ep3.next_puzzles(), [ep4, ep5, ep6])

    def test_is_answer(self):
        epa = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        epw = Puzzle([[2, 3, 1], [5, 4, 6], [0, 8, 7]])
        self.assertTrue(epa.is_answer())
        self.assertFalse(epw.is_answer())

    def test_validate(self):
        ep = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        cpt = [[1, 2, 3], [4, 5, 8], [6, 7, 0]]
        wpt = [[1, 2, 3], [4, 5], [6, 7, 0]]
        self.assertTrue(ep._validate(cpt))
        self.assertFalse(ep._validate(wpt))