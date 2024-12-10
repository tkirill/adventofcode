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
    
    def test_2022_06(self):
        self.assertAocDay(6, '1042', '2980')
    
    def test_2022_07(self):
        self.assertAocDay(7, '1325919', '2050735')
    
    def test_2022_08(self):
        self.assertAocDay(8, '1805', '444528')
    
    def test_2022_09(self):
        self.assertAocDay(9, '6314', '2504')
    
    def test_2022_10(self):
        self.assertAocDay(10, '10760', None)
    
    def test_2022_11(self):
        self.assertAocDay(11, '98280', '17673687232')
    
    def test_2022_12(self):
        self.assertAocDay(12, '391', '386')
    
    def test_2022_13(self):
        self.assertAocDay(13, '5292', '23868')
    
    def test_2022_14(self):
        self.assertAocDay(14, '1406', '20870')
    
    def test_2022_15(self):
        self.assertAocDay(15, '4861076', '10649103160102')
    
    def test_2022_16(self):
        self.assertAocDay(16, '1767', '2528')


if __name__ == '__main__':
    unittest.main()