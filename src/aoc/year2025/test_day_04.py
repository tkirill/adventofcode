import unittest

from aoc.year2025.day_04_Printing_Department import star1, star2


class Year2025_Day04(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(1474, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(8910, actual)


if __name__ == '__main__':
    unittest.main()
