import unittest

from aoc.year2023.day_10_Pipe_Maze import star1, star2


class Year2023_Day10_Pipe_Maze(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(7173, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(291, actual)


if __name__ == '__main__':
    unittest.main()
