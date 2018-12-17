import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    
    def test_bear_01(self):
        self.assertTrue(bears(250))
        self.assertFalse(bears(126))

    '''Tests case exception where the input is 42'''
    def test_bear_42(self):
        self.assertTrue(bears(42))

    '''Tests case exception where the input is less than 42'''
    def test_bear_less42(self):
        self.assertFalse(bears(41))
        
    '''Tests case where no operations are possible on the given input'''
    def test_bear_unoper(self):
        self.assertFalse(bears(53))

    '''Test case for numbers divisible by 2'''
    def test_bear2(self):
        self.assertTrue(bears(208))
        self.assertFalse(bears(82))

    '''Test case for numbers divisible by 3'''
    def test_bear3(self):
        self.assertFalse(bears(126))
        self.assertTrue(bears(168))
        
    '''Test case for numbers divisible by 4'''
    def test_bear4(self):
        self.assertTrue(bears(424))
        self.assertFalse(bears(164))
        
    '''Test case for numbers divisible by 5'''
    def test_bear5(self):
        self.assertTrue(bears(270))
        self.assertFalse(bears(170))
        
    '''Test case for numbers divisible by 2 and 3'''
    def test_bear23(self):
        self.assertTrue(bears(192))
        self.assertFalse(bears(186))
        
    '''Test case for numbers divisble by 2 and 4'''
    def test_bear24(self):
        self.assertTrue(bears(212))
        self.assertFalse(bears(184))
        
    '''Test case for numbers divisible by 2 and 5'''
    def test_bear25(self):
        self.assertTrue(bears(210))
        self.assertFalse(bears(190))
        
    '''Test case for numbers divisible by 3 and 4'''
    def test_bear34(self):
        self.assertTrue(bears(231))
        self.assertFalse(bears(204))
        
    '''Test case for numbers divisible by 3 and 5'''
    def test_bear35(self):
        self.assertTrue(bears(255))
        self.assertFalse(bears(230))
        
    '''Test case for numbers divisible by 4 and 5'''
    def test_bear45(self):
        self.assertTrue(bears(250))
        self.assertFalse(bears(240))
        
    '''Test case for numbers divisible by 2, 3, and 4'''
    def test_bear234(self):
        self.assertTrue(bears(228))
        self.assertFalse(bears(144))
        
    '''Test case for numbers divisible by 2, 3, and 5'''
    def test_bear235(self):
        self.assertTrue(bears(213))
        self.assertFalse(bears(60))
        
    '''Test case for numbers divisible by 2, 4, and 5'''
    def test_bear245(self):
        self.assertTrue(bears(216))
        self.assertFalse(bears(80))
        
    '''Test case for numbers divisible by 3, 4, and 5'''
    def test_bear345(self):
        self.assertTrue(bears(435))
        self.assertFalse(bears(180))
        
    '''Test case for numbers divisible by 2, 3, 4, and 5'''
    def test_bear2345(self):
        self.assertTrue(bears(237))
        self.assertFalse(bears(360))
        

if __name__ == "__main__":
    unittest.main()
