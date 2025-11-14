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
    
    def test_2023_07(self):
        self.assertAocDay(7, '248113761', '246285222')
    
    def test_2023_08(self):
        self.assertAocDay(8, '18827', '20220305520997')
    
    def test_2023_09(self):
        self.assertAocDay(9, '2075724761', '1072')
    
    def test_2023_10(self):
        self.assertAocDay(10, '7173', '291')

    def test_2023_11(self):
        self.assertAocDay(11, '9177603', '632003913611')
    
    def test_2023_12(self):
        self.assertAocDay(12, '7221', '7139671893722')
    
    def test_2023_13(self):
        self.assertAocDay(13, '34993', '29341')
    
    def test_2023_14(self):
        self.assertAocDay(14, '108889', '104671')
    
    def test_2023_15(self):
        self.assertAocDay(15, '516469', '221627')
    
    def test_2023_16(self):
        self.assertAocDay(16, '6740', '7041')
    
    def test_2023_17(self):
        self.assertAocDay(17, '956', '1106')
    
    def test_2023_18(self):
        self.assertAocDay(18, '50465', '82712746433310')
    
    def test_2023_19(self):
        self.assertAocDay(19, '346230', '124693661917133')
    
    def test_2023_20(self):
        self.assertAocDay(20, '866435264', '229215609826339')

    def test_2023_21(self):
        self.assertAocDay(21, '3733', '617729401414635')
    
    def test_2023_22(self):
        self.assertAocDay(22, '446', '60287')
    
    def test_2023_23(self):
        self.assertAocDay(23, '2034', '6302')
    
    def test_2023_24(self):
        self.assertAocDay(24, '15593', '757031940316991')
    
    def test_2023_25(self):
        self.assertAocDay(25, '612945', None)


if __name__ == '__main__':
    unittest.main()