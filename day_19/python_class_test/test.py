import unittest
from main import MyClass

class TsetMyClass(unittest.TestCase):
    
    def test_sum(self):
        mc = MyClass()
        mc.first_num = 1
        mc.second_num = 2
        self.assertEqual(mc.add_num(),3)
        mc.first_num = 1
        mc.second_num = 4
        self.assertEqual(mc.add_num(),3)
        mc.first_num = 2
        mc.second_num = 4
        self.assertEqual(mc.add_num(),1)
        mc.first_num = 2
        mc.second_num = 4
        self.assertEqual(mc.add_num(),8)
        
        

"""
python -m unittest test.py

내코드가 문제없는지 검증

"""