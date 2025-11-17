import unittest

from aoc.year2023.day_09_Mirage_Maintenance import star1, star2


class Year2023_Day09_Mirage_Maintenance(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(2075724761, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(1072, actual)


if __name__ == '__main__':
    unittest.main()
