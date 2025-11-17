import unittest

from aoc.year2023.day_08_Haunted_Wasteland import star1, star2


class Year2023_Day08_Haunted_Wasteland(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(18827, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(20220305520997, actual)


if __name__ == '__main__':
    unittest.main()
