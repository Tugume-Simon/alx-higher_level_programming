#!/usr/bin/python3
"""Test for Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
from io import StringIO
from contextlib import redirect_stdout


class TestRectangleClass(unittest.TestCase):
    """Tests the Rectangle class instances"""

    def setUp(self):
        self.rect = Rectangle(4, 5, 2, 3, 67)

    def tearDown(self):
        """Resets the instances count"""
        Base._Base__nb_objects = 0

    def test_instance_valid(self):
        """tests if instantiation was successful"""
        self.assertTrue(self.rect)

    def test_child_of_Rectangle(self):
        """tests if object is a child of Rectangle class"""
        self.assertTrue(type(self.rect) == Rectangle)

    def test_subclass_of_Base(self):
        """tests if instance is subclass child class"""
        self.assertTrue(issubclass(self.rect.__class__, Base))

    def test_instanse_of_Base(self):
        """tests if object is an instance of the Base class"""
        self.assertTrue(isinstance(self.rect, Base))

    def test_id_from_Base(self):
        """tests if id is dependant on Base when none is provided"""
        Base._Base__nb_objects = 98
        r1 = Rectangle(2, 3)

        self.assertEqual(r1.id, 99)

    def test_id_from_Base_2(self):
        """tests if id when id argument is not provided"""

        r = Rectangle(5, 9)
        self.assertEqual(r.id, 1)

    # --------------Number_of_arguments_passed------------------
    def test_init_without_args(self):
        """tests if instantiation without arguments fails"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_with_one_arg(self):
        """test whether instantiation with one argument fails"""
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_init_with_many_args(self):
        """tests whether instantiation with many arguments fails"""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 78, 3, 4)

    def test_instance_minus_optional_args(self):
        """Tests instance of object minus optional arguments"""
        r1 = Rectangle(3, 2)
        self.assertTrue(r1)

    def test_default_arguments(self):
        """Tests for the assignment of default arguments"""
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_keyworded_arguments(self):
        """Tests if keyword pairs are accepted on instantiating"""
        r = Rectangle(id=89, height=3, x=2, width=8, y=1)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 89)

    # ---------------Type_of_arguments---------------------
    def test_type_arguments(self):
        """Tests for invalid types passed in each of the parameters

        Description: The class __init__ method takes in 5 arguments,
        we need to test for each of the parameters whether the class
        accepts a non-integer type i.e. tuple, boolean, string, list,
        None, set and dictionary.
        For each parameter, the position is attained first and for each
        of the non-integer types to test (in the list 'test_vals'), the
        value is inserted at a position attained in an array 'def_args'
        or other normal integers

        """
        args_list = ['width', 'height', 'x', 'y', 'id']
        def_args = [2, 8, 9, 6]
        test_vals = [(2,), True, "name", 3.14, [3, 4, 5], {3, 5}, None,
                     {'value': 5}, float('-inf'), float('inf'), float('nan')]
        for arg in args_list:
            idx = args_list.index(arg)

            for test in test_vals:
                def_args_copy = def_args.copy()
                if (arg == 'id'):
                    if test is None:
                        continue
                def_args_copy.insert(idx, test)
                with self.assertRaises(TypeError):
                    Rectangle(*def_args_copy)

    # ------------------Value_of_arguments--------------------------
    def test_neg_value_arguments(self):
        """Tests whether negative integral value arguments are invalid"""

        args_list = ['width', 'height', 'x', 'y', 'id']
        def_args = [2, 6, 3, 1]
        test_val = -2
        for arg in args_list:
            idx = args_list.index(arg)
            def_args_copy = def_args.copy()
            def_args_copy.insert(idx, test_val)

            with self.assertRaises(ValueError):
                Rectangle(*def_args_copy)

    def test_zero_value_arguments(self):
        """Tests for zero arguments on id, width and height parameters

        i.e. following the order -> Rectangle(width, height, x, y, id)
        """

        with self.assertRaises(ValueError):
            Rectangle(0, 1, 3, 4, 5)

        with self.assertRaises(ValueError):
            Rectangle(3, 0, 3, 1, 4)

        with self.assertRaises(ValueError):
            Rectangle(2, 4, 0, 2, 0)

    # ------------------Getters_and_Setters--------------------------
    def test_getters_and_setters(self):
        """Tests the getters and setters of the parameters 'id' excluded"""

        r1 = Rectangle(2, 3)
        r1.width = 52
        r1.height = 61
        r1.x = 33
        r1.y = 25

        self.assertEqual(r1.width, 52)
        self.assertEqual(r1.height, 61)
        self.assertEqual(r1.x, 33)
        self.assertEqual(r1.y, 25)
        self.assertEqual(str(r1), '[Rectangle] (1) 33/25 - 52/61')
        self.assertEqual(r1.__dict__, {'_Rectangle__height': 61,
                         '_Rectangle__width': 52, '_Rectangle__x': 33,
                                       '_Rectangle__y': 25, 'id': 1})

    # ------------------Area--------------------------------
    def test_area_with_args(self):
        """Tests if the area method raises an error if args passed"""
        with self.assertRaises(TypeError):
            self.rect.area(1)

    def test_area_proper(self):
        """Tests for correct output of the area method"""
        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.area(), 20)

        w = 101
        h = 6374
        r = Rectangle(w, h)
        self.assertEqual(r.area(), w * h)

    # -------------------Display------------------------------
    def test_display_with_args(self):
        """Tests if the display method raises an error if args passed"""
        with self.assertRaises(TypeError):
            self.rect.display(1)

    def test_display_at_origin(self):
        """Tests the display of rectangle without offsets"""
        r1 = Rectangle(4, 5)
        r2 = Rectangle(10, 3)

        expected_output = "####\n####\n####\n####\n####\n"
        with StringIO() as output, redirect_stdout(output):
            r1.display()
            self.assertEqual(output.getvalue(), expected_output)

        expected_output = "##########\n##########\n##########\n"
        with StringIO() as output, redirect_stdout(output):
            r2.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_display_with_offset(self):
        """Tests the display of rectangle with cordinates"""
        r1 = Rectangle(4, 5, 3, 2)
        r2 = Rectangle(6, 9, 8, 4)

        expected_output = "\n\n" + 5 * (3 * " " + 4 * "#" + "\n")
        with StringIO() as o_buffer, redirect_stdout(o_buffer):
            r1.display()
            self.assertEqual(o_buffer.getvalue(), expected_output)

        expected_output = "\n\n\n\n" + 9 * "        ######\n"

        with StringIO() as o_buffer, redirect_stdout(o_buffer):
            r2.display()
            self.assertEqual(o_buffer.getvalue(), expected_output)

    # ------------------str()----------------------
    def test_str(self):
        """Tests the __str__() function of the Rectangle class"""
        str_rep = self.rect.__str__()
        self.assertEqual(str_rep, "[Rectangle] (67) 2/3 - 4/5")

    def test_str_with_args(self):
        """Tests whether the __str__() function raises error if arg passed"""
        with self.assertRaises(TypeError):
            str_rep = self.rect.__str__('get')

    def test_str_2(self):
        """Tests the __str__() in a different usage"""
        self.assertEqual(str(self.rect), "[Rectangle] (67) 2/3 - 4/5")

    # ----------------update()------------------------------
    def test_update_no_args(self):
        """Tests the update function of the Rectangle class"""
        rect_dict = str(self.rect.__dict__)
        self.rect.update()
        self.assertEqual(str(self.rect.__dict__), rect_dict)

    def test_update_args(self):
        """Tests the update function with args provided"""

        r = Rectangle(2, 4, 0, 0, 1)
        w = r.width
        h = r.height
        x = r.x
        y = r.y
        i = r.id
        r_dict = str(r.__dict__)

        r.update(3, 5, 1, 3, 6)

        self.assertNotEqual(r.width, w)
        self.assertEqual(r.width, 5)
        self.assertNotEqual(r.height, h)
        self.assertEqual(r.height, 1)
        self.assertNotEqual(r.x, x)
        self.assertEqual(r.x, 3)
        self.assertNotEqual(r.y, y)
        self.assertEqual(r.y, 6)
        self.assertNotEqual(r.id, i)
        self.assertEqual(r.id, 3)
        self.assertNotEqual(str(r.__dict__), r_dict)

    def test_update_kwargs(self):
        """Tests the update function with keyword args"""
        r = Rectangle(8, 9, 7, 3, 6)
        w = r.width
        h = r.height
        x = r.x
        y = r.y
        i = r.id
        r.dict = str(r.__dict__)

        r.update(x=2, y=1, id=1, height=21, width=76)

        self.assertNotEqual(r.width, w)
        self.assertEqual(r.width, 76)
        self.assertNotEqual(r.height, h)
        self.assertEqual(r.height, 21)
        self.assertNotEqual(r.x, x)
        self.assertEqual(r.x, 2)
        self.assertNotEqual(r.y, y)
        self.assertEqual(r.y, 1)
        self.assertNotEqual(r.id, i)
        self.assertEqual(r.id, 1)
        self.assertNotEqual(str(r.__dict__), r.dict)

        r.update(y=4, height=3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.height, 3)

        r.update(width=1)
        self.assertEqual(r.width, 1)

    def test_update_less_args(self):
        """Test the update function minus some arguments"""

        r = Rectangle(3, 4, 5, 6, 1)
        r.update(2, 3)

        self.assertEqual(r.width, 3)
        self.assertEqual(r.id, 2)

        r.update(21, 7, 4)
        self.assertEqual(r.id, 21)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 4)

    def test_update_type_errors(self):
        """Tests if update function raises errors for invalid args"""

        r = Rectangle(2, 3, 4, 5, 6)
        args_list = ['id', 'width', 'height', 'x', 'y']
        def_args = [2, 8, 9, 6]
        test_vals = [(2,), True, "name", 3.14, [3, 4, 5], {3, 5}, None,
                     {'value': 5}, float('-inf'), float('inf'), float('nan')]
        for arg in args_list:
            idx = args_list.index(arg)

            for test in test_vals:
                def_args_copy = def_args.copy()
                if (arg == 'id'):
                    if test is None:
                        continue
                def_args_copy.insert(idx, test)
                with self.assertRaises(TypeError):
                    r.update(*def_args_copy)

    def test_neg_value_update(self):
        """Tests whether updated with negatives raises errors"""

        r = Rectangle(3, 4, 5, 6, 7)
        args_list = ['width', 'height', 'x', 'y']
        def_args = [2, 6, 3, 1]
        test_val = -2
        for arg in args_list:
            idx = args_list.index(arg)
            def_args_copy = def_args.copy()
            def_args_copy.insert(idx, test_val)

            with self.assertRaises(ValueError):
                r.update(*def_args_copy)

    def test_zero_value_update(self):
        """Tests for zero update on id, width and height parameters"""

        r = Rectangle(4, 5, 6, 7, 3)
        with self.assertRaises(ValueError):
            r.update(0, 1, 3, 4, 5)

        with self.assertRaises(ValueError):
            r.update(3, 0, 3, 1, 4)

        with self.assertRaises(ValueError):
            r.update(2, 4, 0, 2, 0)

    def test_update_many_args(self):
        """Tests the update function if many args are passed"""
        r = Rectangle(3, 6, 7, 3, 1)
        r.update(3, 5, 6, 3, 6, 7, 8, 2)
        self.assertTrue(r)

    # ---------------to_dictionary------------------
    def test_to_dictionary(self):
        """Tests the to_dictionary() method"""
        r = Rectangle(3, 4, 5, 6, 89)
        self.assertEqual(r.to_dictionary(), {'height': 4, 'id': 89,
                         'width': 3, 'x': 5, 'y': 6})

    def test_to_dictionary_args(self):
        """Tests whether error is raised when args passed"""
        r = Rectangle(3, 2, 1, 6, 89)
        with self.assertRaises(TypeError):
            r.to_dictionary(2)

    def test_to_dictionary_type(self):
        """Tests for the type of to_dictionary()"""
        r = Rectangle(3, 2, 4, 97)
        self.assertTrue(type(r.to_dictionary()) is dict)
