import unittest

from aoc.vector2d import IntVector2D


class TestIntVector2D(unittest.TestCase):

    def test_ctor(self):
        sut = IntVector2D(1, 2)
        self.assertEqual(sut.v1, 1)
        self.assertEqual(sut.v2, 2)
    
    def test_zero(self):
        sut = IntVector2D.zero()
        self.assertEqual(sut.v1, 0)
        self.assertEqual(sut.v2, 0)
    
    def test_same(self):
        sut = IntVector2D.same(1)
        self.assertEqual(sut.v1, 1)
        self.assertEqual(sut.v2, 1)
    
    def test_add_other_type(self):
        sut = IntVector2D.zero()
        self.assertRaises(TypeError, lambda: sut + 'hello')
    
    def test_add_scalar(self):
        sut = IntVector2D.zero()
        actual = sut.increment(1)
        self.assertEqual(actual.v1, 1)
        self.assertEqual(actual.v2, 1)


if __name__ == '__main__':
    unittest.main()
