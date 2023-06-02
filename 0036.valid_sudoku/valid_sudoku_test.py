import unittest
from valid_sudoku import Solution


class TestValidSudoku(unittest.TestCase):
    def test_example1(self):
        self.assertAlmostEqual(Solution().is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                                              , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                              , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                              , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                              , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                              , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                              , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                              , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                              , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]), True)

    def test_example2(self):
        self.assertAlmostEqual(Solution().is_valid_sudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                                              , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                              , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                              , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                              , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                              , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                              , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                              , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                              , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]), False)