#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from copy import deepcopy

from eight.puzzle import Puzzle


class PuzzleIDAStarSolver(object):

    def __init__(self, puzzle, heuristic_func):
        puzzle.hs = heuristic_func(puzzle)
        puzzle.fs = puzzle.hs
        self.expand_n = 0
        self.heuristic = heuristic_func
        self.puzzles = [puzzle]
        self.root = puzzle

    def _solve_df(self, puzzle, f_limit, route):
        """深さ優先探索"""
        # f が limit を超えていれば探索失敗
        if puzzle.fs > f_limit:
            return (None, puzzle.fs)

        # 答えであれば探索終了
        if puzzle.is_answer():
            return (route, f_limit)

        next_f_limit = float('inf')

        # 展開回数を記録
        self.expand_n += 1
        puzzle = self.puzzles[self.puzzles.index(puzzle)]
        puzzle.n.append(self.expand_n)

        next_puzzles = sorted(puzzle.next_puzzles(), key=lambda p: 1 + p.hs)

        for np in next_puzzles:
            np.parent = puzzle
            np.gs = puzzle.gs + 1
            np.hs = self.heuristic(np)
            np.fs = np.gs + np.hs
            if np not in self.puzzles:
                self.puzzles.append(np)

        for np in next_puzzles:
            solution, new_cost_limit = self._solve_df(
                np, f_limit, route + [np])
            if solution is not None:
                return (solution, new_cost_limit)
            next_f_limit = min(next_f_limit, new_cost_limit)
        return (None, next_f_limit)

    def solve(self):
        bound = self.root.hs
        self.root.gs = 0
        self.root.fs = self.root.hs
        while True:
            solution, bound = self._solve_df(self.root, bound, [self.root])
            if solution is not None:
                return solution
            if bound == float('inf'):
                return None
        return []


class PuzzleAStarSolver(object):

    def __init__(self, puzzle, heuristic_func):
        puzzle.gs = 0
        puzzle.hs = heuristic_func(puzzle)
        puzzle.fs = puzzle.gs + puzzle.hs
        self.open_puzzles = [puzzle]
        self.close_puzzles = []
        self.heuristic = heuristic_func

    def solve(self):
        # 展開回数
        expand_n = 0
        # Open が空になるまで繰り返す
        while len(self.open_puzzles) > 0:
            # Open の中で f(n) 最小のものを取り出す
            puzzle = min(self.open_puzzles, key=lambda x: x.fs)

            # 答えであれば探索終了
            if puzzle.is_answer():
                # 答えから順に親を辿っていって, 解答のリストを作成する
                route = [puzzle]
                while puzzle.parent is not None:
                    route.insert(0, puzzle.parent)
                    puzzle = puzzle.parent
                return deepcopy(route)

            # 取り出したパズルを Close に移動
            self.open_puzzles.remove(puzzle)
            self.close_puzzles.append(puzzle)

            # 取り出したパズルの g* を計算
            puzzle.gs = puzzle.fs - puzzle.hs

            # パズルを展開して次の状態を求める
            expand_n += 1
            puzzle.n = [expand_n]
            for p in puzzle.next_puzzles():
                # 次状態の f を求める
                p.hs = self.heuristic(p)
                fd = puzzle.gs + p.hs + 1
                p.fs = fd
                p.parent = puzzle
                if p in self.open_puzzles:
                    q = self.open_puzzles[self.open_puzzles.index(p)]
                    if q.fs > fd:
                        # Open に f がより大きいものがあれば置換
                        self.open_puzzles.remove(p)
                        self.open_puzzles.append(p)
                elif p in self.close_puzzles:
                    q = self.close_puzzles[self.close_puzzles.index(p)]
                    if q.fs > fd:
                        # Close に f がより大きいものがあれば置換して Open に
                        self.close_puzzles.remove(p)
                        self.open_puzzles.append(p)
                else:
                    # 新しい盤面であれば Open に追加
                    self.open_puzzles.append(p)
        return None
