#!/usr/bin/python3
"""Base class unit test"""
from models.base import Base
import unittest


class TestBaseClass(unittest.TestCase):
    """Tests the Base class of the models package"""
    
    def setUp(self):
        self.obj = Base(89)

    def tearDown(self):
        """resets the Base class"""
        Base._Base__nb_objects = 0

    def test_object_instance(self):
        """tests for instance of the Base class"""
        self.assertTrue(isinstance(self.obj, Base))

    def test_base_init_no_args(self):
        """Tests initialization of Base class without arguments"""
        myObject = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 1)

    def test_base_instance_count_update(self):
        """tests for update of __nb_objects attribute"""
        obj1 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 1)

        obj2 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)

        obj3 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 3)

    def test_init_id_increment(self):
        """tests if ids assigned are incremented by 1"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

        obj3 = Base()
        self.assertEqual(obj2.id + 1, obj3.id)

    def test_id_count_synced(self):
        """tests whether ids assigned are equal to class instance count"""
        obj1 = Base()
        self.assertEqual(obj1.id, getattr(Base, "_Base__nb_objects"))

        obj2 = Base()
        self.assertEqual(obj2.id, getattr(Base, "_Base__nb_objects"))

    def test_id_value_arg_given(self):
        """tests whether id given is set"""

        n = 67
        obj = Base(n)
        self.assertEqual(obj.id, n)

    def test_base_init_many_args(self):
        """tests for exception the if many args are given"""
        with self.assertRaises(TypeError):
            Base(1, 2)
