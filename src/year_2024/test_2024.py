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
    
    def test_2024_07(self):
        self.assertAocDay(7, '6392012777720', '61561126043536')
    
    def test_2024_08(self):
        self.assertAocDay(8, '256', '1005')
    
    def test_2024_09(self):
        self.assertAocDay(9, '6241633730082', '6265214124644')
    
    def test_2024_10(self):
        self.assertAocDay(10, '794', '1706')
    
    def test_2024_11(self):
        self.assertAocDay(11, '194557', '231532558973909')
    
    def test_2024_12(self):
        self.assertAocDay(12, '1370258', '805814')
    
    def test_2024_13(self):
        self.assertAocDay(13, '40369', '72587986598368')
    
    def test_2024_14(self):
        self.assertAocDay(14, '226179492', '7502')
    
    def test_2024_15(self):
        self.assertAocDay(15, '1441031', '1425169')
    
    def test_2024_15(self):
        self.assertAocDay(16, '83444', '483')


if __name__ == '__main__':
    unittest.main()