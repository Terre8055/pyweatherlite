import unittest
from src.pyweatherlite.helpers import SetContextData
from src.pyweatherlite.Base import BaseClass

class TestHelpers(unittest.TestCase):
    """Class testcases for helper procedures"""

    def test_class_docstrings(self):
        doctest = SetContextData()
        self.assertTrue(len(doctest.set_coordinates.__doc__) > 5)
        self.assertTrue(len(SetContextData.__doc__) > 5)


    def test_subclassdata(self):
        """Test subclasses and its attributes"""
        s= SetContextData()
        self.assertTrue(issubclass(SetContextData, BaseClass))
        self.assertTrue(hasattr(s, "_longitude"))
        self.assertTrue(hasattr(s, "_latitude"))
        self.assertFalse(hasattr(s, "_age"))
    
    def test_coordinates(self):
        s = SetContextData()
        s.set_coordinates(2.55)
        self.assertEqual(s.get_latitude, 0.00)
        self.assertIsNotNone(s.get_latitude)
        self.assertNotEqual(s.get_latitude, 2.55)
        self.assertEqual(s.get_longitude, 2.55)
        self.assertIsNotNone(s.get_longitude)
        self.assertNotEqual(s.get_longitude, 1.55)

    
    def test_open_coords_url(self):
        """Test url api for coords"""
        s = SetContextData()
        s.open_coords_url('a98d0f2d0f6973a5203ba90cff1f2807')
        self.assertNotEqual(s.get_latitude, 0.00)
        self.assertNotEqual(s.get_longitude, 0.00)
        self.assertIsNotNone(s.get_latitude)
        self.assertIsNotNone(s.get_longitude)
        self.assertTrue(type(s.get_latitude), float)
        self.assertTrue(type(s.get_longitude), float)



