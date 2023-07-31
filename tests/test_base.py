import unittest
from src.pyweatherlite.Base import BaseClass


class TestBaseClass(unittest.TestCase):
    """Class for Testing BaseClass module"""

    def test_class_docstrings(self):
        doctest = BaseClass()
        self.assertTrue(len(doctest.get_latitude.__doc__) > 5)
        self.assertTrue(len(doctest.get_longitude.__doc__) > 5)
        self.assertTrue(len(BaseClass.__doc__) > 5)

    def test_class_instanse(self):
        """Test instances of BaseClass"""
        b1 = BaseClass()
        self.assertEqual(isinstance(b1, BaseClass), True)
        self.assertEqual(type(b1._longitude), float)
        self.assertEqual(type(b1._latitude), float)

    def test_get_longitude(self):
        """Test getter for long coords"""
        c= BaseClass()
        self.assertEqual(type(c._longitude), float)
        self.assertEqual(type(c._latitude), float)
        self.assertIsNotNone(c.get_longitude)

    def test_get_latitude(self):
        """Test getter for lat coords"""
        c= BaseClass()
        self.assertEqual(type(c._longitude), float)
        self.assertEqual(type(c._latitude), float)
        self.assertIsNotNone(c.get_latitude)





