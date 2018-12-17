import unittest
from perm_lex import perm_gen_lex

class TestAssign1(unittest.TestCase):
    
    '''Tests empty list case exception'''
    def test_perm_gen_lex_empty(self):
        self.assertEqual(perm_gen_lex(''), [])

    '''Tests cases where the list is of length 1'''
    def test_perm_gen_lex_one(self):
        self.assertEqual(perm_gen_lex('a'), ['a'])
        
    '''Tests cases where the list is of length 2'''
    def test_perm_gen_lex_two(self):
        self.assertEqual(perm_gen_lex('ab'),['ab','ba'])

    '''Tests cases where the list is of length 3'''
    def test_perm_gen_lex_three(self):
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    '''Tests cases where the list is of length 4'''
    def test_perm_gen_lex_four(self):
        self.assertEqual(perm_gen_lex('fqyz'), ['fqyz', 'fqzy', 'fyqz', 'fyzq', 'fzqy', 'fzyq', 'qfyz', 'qfzy', 'qyfz', 'qyzf', 'qzfy', 'qzyf', 'yfqz', 'yfzq', 'yqfz', 'yqzf', 'yzfq', 'yzqf', 'zfqy', 'zfyq', 'zqfy', 'zqyf', 'zyfq', 'zyqf']) 

    '''Tests cases where the list is comprised of non-sequential letters'''
    def test_perm_gen_lex_non_seq(self):
        self.assertEqual(perm_gen_lex('dlz'), ['dlz', 'dzl', 'ldz', 'lzd', 'zdl', 'zld'])
    

if __name__ == "__main__":
        unittest.main()
