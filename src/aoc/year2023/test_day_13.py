import unittest

from aoc.year2023.day_13_Point_of_Incidence import star1, star2


class Year2023_Day13_Point_of_Incidence(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(34993, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(29341, actual)


if __name__ == '__main__':
    unittest.main()
