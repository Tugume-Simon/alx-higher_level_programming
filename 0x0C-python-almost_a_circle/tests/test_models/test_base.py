#!/usr/bin/python3
"""Base class unit test"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
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

    #--------------to_json_string----------------------
    def test_to_json_string_proper(self):
        """Tests the to_json_string method with right arguments"""
        r = Rectangle(4, 5, 1, 2, 89)
        s = Square(3, 4, 1, 67)

        self.assertEqual(Base.to_json_string([{'height': 3}, {'width': 3}]),
            '[{"height": 3}, {"width": 3}]')

        dicts = list([r.to_dictionary(), s.to_dictionary()])
        self.assertEqual(Base.to_json_string(dicts),
                '''[{"id": 89, "width": 4, "height": 5, "x": 1, "y": 2},\
 {"id": 67, "size": 3, "x": 4, "y": 1}]''')

    def test_to_json_string_format(self):
        """Tests if the output is in json format"""
        r = Rectangle(4, 5, 1, 2, 89)
        output = Base.to_json_string([r.to_dictionary()])
        self.assertTrue(json.loads(output))

    def test_to_json_string_non_lists(self):
        """Tests if non-list types, apart from -None- do not pass"""
        non_list_types = [1.4, 2, 'taggy', {7, 3, 5}, True, {'clock': 4},
                (2, 3, 4), float('inf'), float('nan'), float('-inf')]

        for test_type in non_list_types:
            with self.assertRaises(TypeError):
                Base.to_json_string(test_type)

    def test_to_json_string_none_type(self):
        """Tests whether an empty list is returned when None is passed"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_lists_auth(self):
        """Tests for possible lists whether they are rejected by the function

        - list of integers
        - list of floats
        - list of lists
        - list of strings
        - list of tuples
        - list of sets
        """
        l_ints = [1, 2, 3, 4]
        l_floats = [1.2, 0.4, 8.7, 3.4]
        l_strings = ['hello', 'holberton', 'betty']
        l_tuples = [(2, 4), (8, 9, 3), (4,)]
        l_sets = [{2, 4}, {4, 5}, {8, 4, 4}]
        l_lists = [[3, 1, 2, 4], [4, 6, 7], [4, 5]]

        l_all = [l_ints, l_floats, l_strings, l_tuples, l_sets, l_lists]

        for test_list in l_all:
            with self.assertRaises(TypeError):
                Base.to_json_string(test_list)

    def test_to_json_string_empty_list(self):
        """Tests whether an empty list is returned if an empty list is passed"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_many_arguments(self):
        """Tests whether error is raised if many arguments are passed"""
        with self.assertRaises(TypeError):
            Base.to_json_string([{'name': True}, {'age': 8}], [])

    #-------------------save_to_file-------------------
    def test_save_to_file_no_args(self):
        """Tests call to the function without arguments"""
        with self.assertRaises(TypeError):
            Base.save_to_file()
            
    def test_save_to_file_many_args(self):
        """Tests call to the function with many arguments"""
        r = Rectangle(3, 5)
        s = Square(3)

        with self.assertRaises(TypeError):
            Base.save_to_file([r, s], [])

    def test_save_to_file_type_list(self):
        """Tests for possible lists whether they are rejected by the function

        - list of integers
        - list of floats
        - list of lists
        - list of strings
        - list of tuples
        - list of sets
        """
        l_ints = [1, 2, 3, 4]
        l_floats = [1.2, 0.4, 8.7, 3.4]
        l_strings = ['hello', 'holberton', 'betty']
        l_tuples = [(2, 4), (8, 9, 3), (4,)]
        l_sets = [{2, 4}, {4, 5}, {8, 4, 4}]
        l_lists = [[3, 1, 2, 4], [4, 6, 7], [4, 5]]

        l_all = [l_ints, l_floats, l_strings, l_tuples, l_sets, l_lists]

        for test_list in l_all:
            with self.assertRaises(TypeError):
                Base.save_to_file(test_list)

