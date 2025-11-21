import unittest

from aoc.year2023.day_12_Hot_Springs import star1, star2


class Year2023_Day12_Hot_Springs(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(7221, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(7139671893722, actual)


if __name__ == '__main__':
    unittest.main()
