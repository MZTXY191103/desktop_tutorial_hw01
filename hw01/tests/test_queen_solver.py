import sys
sys.path.append("..")  # 把 hw01 目录加入搜索路径

import unittest
from src.queen_solver import solve_n_queens

class TestNQueens(unittest.TestCase):
    def test_4_queens(self):
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2, "4 皇后应有 2 个解")

    def test_8_queens(self):
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92, "8 皇后应有 92 个解")

if __name__ == "__main__":
    unittest.main()