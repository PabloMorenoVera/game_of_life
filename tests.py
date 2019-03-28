import unittest as ut
from game_of_life import GameOfLife

class TestGameOfLife(ut.TestCase):
    def test_Dim_10(self):
        gol = GameOfLife(N=10)
        gol.main()

    def test_Dim_20(self):
        gol = GameOfLife(N=20)
        gol.main()

    def test_Dim_50(self):
        gol = GameOfLife(N=50)
        gol.main()

    def test_Dim_100(self):
        gol = GameOfLife(N=100)
        gol.main()

if __name__ == '__main__':
    ut.main()
