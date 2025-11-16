import unittest

from aoc.year2023.day_06_Wait_For_It import star1, star2


class Year2023_Day06_Wait_For_It(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(3316275, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(27102791, actual)


if __name__ == '__main__':
    unittest.main()
