import unittest

from aoc.vector2d import IntVector2D


class TestIntVector2D(unittest.TestCase):

    def test_ctor(self):
        sut = IntVector2D(1, 2)
        self.assertEqual(sut.v1, 1)
        self.assertEqual(sut.v2, 2)


if __name__ == '__main__':
    unittest.main()
