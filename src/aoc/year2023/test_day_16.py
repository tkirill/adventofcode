import unittest

from aoc.year2023.day_16_The_Floor_Will_Be_Lava import star1, star2


class Year2023_Day16_The_Floor_Will_Be_Lava(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(6740, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(7041, actual)


if __name__ == '__main__':
    unittest.main()
