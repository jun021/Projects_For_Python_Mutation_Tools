import unittest
import tri
class CalcTest(unittest.TestCase):
    #scalene
    def test_triangle_type_scalene(self):
        self.assertEqual(tri.triangle_type(2,3,4), "1=scalene")
    #isosceles
    def test_triangle_type_isosceles(self):
        self.assertEqual(tri.triangle_type(3,3,2), "2=isosceles")
    #equilateral
    def test_triangle_type_equilateral(self):
        self.assertEqual(tri.triangle_type(3,3,3), "3=equilateral")
    #error for negative sides
    def test_triangle_type_negative_sides(self):
        self.assertEqual(tri.triangle_type(-1,3,4), "4=error")
        self.assertEqual(tri.triangle_type(1,-2,3), "4=error")
        self.assertEqual(tri.triangle_type(1,2,-4), "4=error")
    #error for mismatching the condition for building triangle
    def test_triangle_type_wrong_condiion(self):
        self.assertEqual(tri.triangle_type(10,2,3), "4=error")
        self.assertEqual(tri.triangle_type(1,10,2), "4=error")
        self.assertEqual(tri.triangle_type(1,2,10), "4=error")