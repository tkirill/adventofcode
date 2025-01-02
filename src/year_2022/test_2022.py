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
    
    def test_2022_17(self):
        self.assertAocDay(17, '3090', '1530057803453')
    
    def test_2022_18(self):
        self.assertAocDay(18, '4310', '2466')
    
    def test_2022_19(self):
        self.assertAocDay(19, '1550', '18630')
    
    def test_2022_20(self):
        self.assertAocDay(20, '4151', '7848878698663')
    
    def test_2022_21(self):
        self.assertAocDay(21, '170237589447588', '3712643961892')
    
    def test_2022_22(self):
        self.assertAocDay(22, '36518', '143208')
    
    def test_2022_23(self):
        self.assertAocDay(23, '3874', '948')
    
    def test_2022_24(self):
        self.assertAocDay(24, '245', '798')
    
    def test_2022_25(self):
        self.assertAocDay(25, '20-1-0=-2=-2220=0011', None)


if __name__ == '__main__':
    unittest.main()