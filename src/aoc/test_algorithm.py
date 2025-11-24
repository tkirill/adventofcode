import unittest

from aoc.algorithm import nth_with_cycle


class AlgorithmTests(unittest.TestCase):

    def test_nth_with_cycle(self):
        values = list(range(13)) + list(range(13,13+17))*3
        for i, v in enumerate(values):
            self.assertEqual(v, nth_with_cycle(values, i))


if __name__ == '__main__':
    unittest.main()
