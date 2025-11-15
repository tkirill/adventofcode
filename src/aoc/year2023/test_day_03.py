import unittest

from aoc.year2023.day_03_Gear_Ratios import star1, star2


class Year2023_Day03_Gear_Ratios(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(550934, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(81997870, actual)


if __name__ == '__main__':
    unittest.main()
