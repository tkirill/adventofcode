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
    
    def test_2024_16(self):
        self.assertAocDay(16, '83444', '483')
    
    def test_2024_17(self):
        self.assertAocDay(17, '3,3,7,3,6,3,6,0,2', '105843716614554')
    
    def test_2024_18(self):
        self.assertAocDay(18, '284', '51,50')
    
    def test_2024_19(self):
        self.assertAocDay(19, '319', '692575723305545')
    
    def test_2024_20(self):
        self.assertAocDay(20, '1399', '994807')
    
    def test_2024_21(self):
        self.assertAocDay(21, '238078', '293919502998014')
    
    def test_2024_22(self):
        self.assertAocDay(22, '17163502021', '1938')
    
    def test_2024_23(self):
        self.assertAocDay(23, '926', 'az,ed,hz,it,ld,nh,pc,td,ty,ux,wc,yg,zz')
    
    def test_2024_24(self):
        self.assertAocFile('24_Crossed_Wires.py', '43559017878162', 'fhc,ggt,hqk,mwh,qhj,z06,z11,z35')


if __name__ == '__main__':
    unittest.main()