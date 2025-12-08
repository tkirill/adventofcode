import unittest

from aoc.year2025.day_08_Playground import star1, star2


class Year2025_Day05(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(84968, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(8663467782, actual)


if __name__ == '__main__':
    unittest.main()
