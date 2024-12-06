import unittest
from pathlib import Path

from aoc.aoc_test_base import AocTestBase


class TestYear2023(AocTestBase):

    def setUp(self):
        self.test_dir = Path(__file__).parent
        return super().setUp()

    def test_2023_01(self):
        self.assertAocDay(1, '54667', '54203')
    
    def test_2023_02(self):
        self.assertAocDay(2, '2563', '70768')
    
    def test_2023_03(self):
        self.assertAocDay(3, '550934', '81997870')
    
    def test_2023_04(self):
        self.assertAocDay(4, '19135', '5704953')
    
    def test_2023_05(self):
        self.assertAocDay(5, '600279879', '20191102')
    
    def test_2023_06(self):
        self.assertAocDay(6, '3316275', '27102791')


if __name__ == '__main__':
    unittest.main()