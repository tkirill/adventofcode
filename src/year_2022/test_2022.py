import unittest
from pathlib import Path

from aoc.aoc_test_base import AocTestBase


class TestYear2022(AocTestBase):

    def setUp(self):
        self.test_dir = Path(__file__).parent
        return super().setUp()

    def test_2022_01(self):
        self.assertAocDay(1, '67450', '199357')
    
    def test_2022_02(self):
        self.assertAocDay(2, '8392', '10116')
    
    def test_2022_03(self):
        self.assertAocDay(3, '7737', '2697')
    
    def test_2022_04(self):
        self.assertAocDay(4, '538', '792')
    
    def test_2022_05(self):
        self.assertAocDay(5, 'RNZLFZSJH', 'CNSFCGJSM')


if __name__ == '__main__':
    unittest.main()