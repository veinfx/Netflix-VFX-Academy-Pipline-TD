import unittest
import unit_test

class MyCalTest(unittest.TestCase):
    def test_add(self):
        c = unit_test.add(20,10)
        self.assertEqual(c, 30)

    def test_sub(self):
        c = unit_test.sub(20,10)
        self.assertEqual(c,10)

if __name__ == '__main__':
    unittest.main()