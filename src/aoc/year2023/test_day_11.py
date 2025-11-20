import unittest

from aoc.year2023.day_11_Cosmic_Expansion import star1, star2


class Year2023_Day11_Cosmic_Expansion(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(9177603, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(632003913611, actual)


if __name__ == '__main__':
    unittest.main()
