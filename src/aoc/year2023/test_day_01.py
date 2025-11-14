import unittest

from aoc.year2023.day_01_Trebuchet import star1, star2


class Year2023_Day01_Trebuchet(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(54667, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(54203, actual)


if __name__ == '__main__':
    unittest.main()