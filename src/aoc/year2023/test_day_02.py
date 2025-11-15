import unittest

from aoc.year2023.day_02_Cube_Conundrum import star1, star2


class Year2023_Day02_Cube_Conundrum(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(2563, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(70768, actual)


if __name__ == '__main__':
    unittest.main()