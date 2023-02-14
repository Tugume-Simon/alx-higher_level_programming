#!/usr/bin/python3
"""Square class Test"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquareClass(unittest.TestCase):
    """Tests the class Square of the models package"""

    def setUp(self):
        self.square1 = Square(5, 2, 1, 89)

    
