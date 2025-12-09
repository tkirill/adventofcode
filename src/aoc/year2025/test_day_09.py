import unittest

from aoc.year2025.day_09_Movie_Theater import star1, star2


class Year2025_Day09(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(4761736832, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
