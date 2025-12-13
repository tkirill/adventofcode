import unittest

from aoc.year2023.day_19_Aplenty import star1, star2


class Year2023_Day17(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(346230, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(124693661917133, actual)


if __name__ == '__main__':
    unittest.main()
