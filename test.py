import unittest
from lab2 import Weight


class TestProgression(unittest.TestCase):
    test = Weight(2.56)
    def test_add__(self):
        self.assertEqual(self.test.__add__(3), 0.0556)
        self.assertEqual(self.test.__add__(2.44), 0.05)
        self.assertTrue(self.test.__add__(487), isinstance(self.test.__add__(487), float))

    def test_sub__(self):
        self.assertEqual(self.test.__sub__(2), 0.005600000000000001)
        self.assertEqual(self.test.__sub__(1), 0.015600000000000001)
        self.assertRaises(ValueError, self.test.__sub__, 6)


    def test_mul__(self):
        self.assertEqual(self.test.__mul__(2), 0.000512)
        self.assertEqual(self.test.__mul__(4), 0.001024)




if __name__ == '__main__':
    unittest.main()
