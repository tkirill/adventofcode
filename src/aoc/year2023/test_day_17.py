import unittest

from aoc.year2023.day_17_Clumsy_Crucible import star1, star2


class Year2023_Day17(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(956, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(1106, actual)


if __name__ == '__main__':
    unittest.main()
