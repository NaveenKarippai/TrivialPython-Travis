from one import fun
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 8)

if __name__ == '__main__':
    unittest.main()