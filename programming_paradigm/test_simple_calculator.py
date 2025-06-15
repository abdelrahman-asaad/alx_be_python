import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.calc = SimpleCalculator()             #creating object from SimpleCalculator class
        self.assertEqual(self.calc.add(2, 3), 5)
    def test_subtarction(self):
        self.calc = SimpleCalculator()             #creating object from SimpleCalculator class
        self.assertEqual(self.calc.multiply(6, 3), 3)
    def test_multiblication(self):
        self.calc = SimpleCalculator()             #creating object from SimpleCalculator class
        self.assertEqual(self.calc.add(2, 3), 6)
    def test_division (self):
        self.calc = SimpleCalculator()             #creating object from SimpleCalculator class
        self.assertEqual(self.calc.add(6, 3), 2)
        


#import unittest
#from simple_calculator import SimpleCalculator

#class TestSimpleCalculator(unittest.TestCase):
#    def test_add(self,adding):
#        adding = SimpleCalculator.add(5,7)
#        self.assertEqual(adding, 12)
#    def test_subtarction(self,subtraction):
#        subtraction = SimpleCalculator.subtract(12, 2)
#        self.assertEqual(subtraction, 10)
#    def test_multiblication(self, multiblacation):
#        multiblacation = SimpleCalculator.multiply(5,7)
#        self.assertEqual(multiblacation, 35)
#    def test_division (self, division):
#        division = SimpleCalculator.divide(10, 2)    
#        self.assertEqual(division, 5)
        
        