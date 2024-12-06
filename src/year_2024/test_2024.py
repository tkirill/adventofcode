import unittest
from pathlib import Path

from aoc.aoc_test_base import AocTestBase


class TestYear2024(AocTestBase):

    def setUp(self):
        self.test_dir = Path(__file__).parent
        return super().setUp()

    def test_2024_01(self):
        self.assertAocDay(1, '936063', '23150395')
    
    def test_2024_02(self):
        self.assertAocDay(2, '624', '658')
    
    def test_2024_03(self):
        self.assertAocDay(3, '178886550', '87163705')
    
    def test_2024_04(self):
        self.assertAocDay(4, '2573', '1850')
    
    def test_2024_05(self):
        self.assertAocDay(5, '6949', '4145')
    
    def test_2024_06(self):
        self.assertAocDay(6, '4374', '1705')


if __name__ == '__main__':
    unittest.main()