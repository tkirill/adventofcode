import unittest

from aoc.year2023.day_05_Seeds import star1, star2


class Year2023_Day04_Seeds(unittest.TestCase):

    def testStar1(self):
        actual = star1()
        self.assertEqual(600279879, actual)
    
    def testStar2(self):
        actual = star2()
        self.assertEqual(20191102, actual)


if __name__ == '__main__':
    unittest.main()
