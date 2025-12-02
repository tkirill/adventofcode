import unittest

from aoc.year2025.day_02_Gift_Shop import star1, star2


class Year2025_Day02_Gift_Shop(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(40055209690, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(50857215650, actual)


if __name__ == '__main__':
    unittest.main()
