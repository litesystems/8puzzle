#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

from eight import heuristic
from eight.puzzle import Puzzle
from eight.solver import PuzzleAStarSolver, PuzzleIDAStarSolver



class TestPuzzleAStarSolver(unittest.TestCase):
    def test_solve(self):
        puzzle = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]
        expected = [
            Puzzle([[1, 0, 3], [4, 2, 6], [7, 5, 8]]),
            Puzzle([[1, 2, 3], [4, 0, 6], [7, 5, 8]]),
            Puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]]),
            Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        ]
        solver = PuzzleAStarSolver(Puzzle(puzzle), heuristic.diff)
        answer = solver.solve()
        for a, e in zip(answer, expected):
            self.assertEqual(a, e)
        solver = PuzzleAStarSolver(Puzzle(puzzle), heuristic.manhattan)
        answer = solver.solve()
        for a, e in zip(answer, expected):
            self.assertEqual(a, e)


class TestPuzzleIDAStarSolver(unittest.TestCase):
    def test_solve(self):
        puzzle = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]
        expected = [
            Puzzle([[1, 0, 3], [4, 2, 6], [7, 5, 8]]),
            Puzzle([[1, 2, 3], [4, 0, 6], [7, 5, 8]]),
            Puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]]),
            Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        ]
        solver = PuzzleIDAStarSolver(Puzzle(puzzle), heuristic.diff)
        answer = solver.solve()
        for a, e in zip(answer, expected):
            self.assertEqual(a, e)
        solver = PuzzleIDAStarSolver(Puzzle(puzzle), heuristic.manhattan)
        answer = solver.solve()
        for a, e in zip(answer, expected):
            self.assertEqual(a, e)
