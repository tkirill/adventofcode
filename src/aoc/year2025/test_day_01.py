import unittest

from aoc.year2025.day_01_Secret_Entrance import star1, star2


class Year2025_Day01_Trebuchet(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(1139, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(6684, actual)


if __name__ == '__main__':
    unittest.main()
