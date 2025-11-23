import unittest

from aoc.year2023.day_14_Parabolic_Reflector_Dish import star1, star2


class Year2023_Day14_Parabolic_Reflector_Dish(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(108889, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(104671, actual)


if __name__ == '__main__':
    unittest.main()
