import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    '''Tests for conversion with num = 0'''
    def test_num0(self):
        self.assertEqual(convert(0, 4), "0")
        
    '''Tests for conversion with base 2'''
    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    '''Tests for conversion with base 3'''
    def test_base3(self):
        self.assertEqual(convert(70,3),"2121")

    '''Tests for conversion with base 4'''
    def test_base4(self):
        self.assertEqual(convert(316,4),"10330")

    '''Tests for conversion with base 5'''
    def test_base5(self):
        self.assertEqual(convert(83,5), "313")
        
    '''Tests for conversion with base 6'''
    def test_base6(self):
        self.assertEqual(convert(219,6), "1003")
        
    '''Tests for conversion with base 7'''
    def test_base7(self):
        self.assertEqual(convert(68, 7), "125")
        
    '''Tests for conversion with base 8'''
    def test_base8(self):
        self.assertEqual(convert(94, 8), "136")
        
    '''Tests for conversion with base 9'''
    def test_base9(self):
        self.assertEqual(convert(548, 9), "668")
        
    '''Tests for conversion with base 10'''
    def test_base10(self):
        self.assertEqual(convert(892, 10), "892")
        
    '''Tests for conversion with base 11'''
    def test_base11(self):
        self.assertEqual(convert(389, 11), "324")
        
    '''Tests for conversion with base 12'''
    def test_base12(self):
        self.assertEqual(convert(174, 12), "126")
        
    '''Tests for conversion with base 13'''
    def test_base13(self):
        self.assertEqual(convert(364, 13), "220")
        
    '''Tests for conversion with base 14'''
    def test_base14(self):
        self.assertEqual(convert(945, 14), "4B7")
        
    '''Tests for conversion with base 15'''
    def test_base15(self):
        self.assertEqual(convert(632, 15), "2C2")
        
    '''Tests for conversion with base 16'''
    def test_base16(self):
        self.assertEqual(convert(754, 16), "2F2")

    def test_base_with0(self):
        self.assertEqual(convert(906, 3), "1020120")
        
if __name__ == "__main__":
        unittest.main()
