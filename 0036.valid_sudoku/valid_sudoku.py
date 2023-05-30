"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
"""
import collections
from typing import List
import numpy as np


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows or
                    board[r][c] in cols or
                    board[r][c] in squares[(r//3, c//3)]):
                        return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
