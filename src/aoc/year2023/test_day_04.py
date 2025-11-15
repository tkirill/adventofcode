import unittest

from aoc.year2023.day_04_Scratchcards import star1, star2


class Year2023_Day04_Scratchcards(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(19135, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(5704953, actual)


if __name__ == '__main__':
    unittest.main()
