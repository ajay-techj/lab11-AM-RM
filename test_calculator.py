# https://github.com/ajay-techj/lab11-AM-RM.git
# Partner 1: Ajay Manam
# Partner 2: Ryan Malkani
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(3, 3), 6)
        self.assertEqual(add(4, 3), 7)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), 5)
        self.assertEqual(subtract(3, 3), 6)
        self.assertEqual(subtract(4, 3), 7)

    ######## Partner 1
     def test_multiply(self): # 3 assertions
         self.assertEqual(mul(4,5), 20) 
         self.assertEqual(mul(9,10), 90)
         self.assertEqual(mul(11,1), 11)

     def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(10,2),5)
        self.assertAlmostEqual(div(4,4),1)
        self.assertAlmostEqual(div(9,3),3)
    # ##########################


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self):
        self.assertAlmostEqual(subtract(2, 8), 3)
        self.assertAlmostEqual(subtract(10, 100), 2)
        self.assertAlmostEqual(subtract(3, 81), 4)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            div(-2, 8)
    
    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

     def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual((hypotenuse(3,4),5))
        self.assertAlmostEqual((hypotenuse(5,12),13))
        self.assertAlmostEqual((hypotenuse(0,1),1))
    #     fill in code

     def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(25), 5)
    #     fill in code
    ##########################


if __name__ == "__main__":
    unittest.main()