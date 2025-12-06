import unittest

from aoc.year2025.day_06_Trash_Compactor import star1, star2


class Year2025_Day05(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(4722948564882, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(9581313737063, actual)


if __name__ == '__main__':
    unittest.main()
