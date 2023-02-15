#!/usr/bin/python3
"""Square class Test"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquareClass(unittest.TestCase):
    """Tests the class Square of the models package"""

    def setUp(self):
        self.square = Square(5, 2, 1, 89)

    def tearDown(self):
        """Resets the instances count"""
        Base._Base_nb_objects = 0
    
    def test_instance_valid(self):
        """test if instantiation works"""
        self.assertTrue(self.square)

    def test_if_square_object(self):
        """tests if instance is of square class"""
        self.assertTrue(type(self.square) == Square)

    def test_is_subclass_of_square(self):
        """tests if instance is a subclass of Square"""
        clss = self.square.__class__
        self.assertTrue(issubclass(clss, Square))

    def test_is_subclass_of_rectangle(self):
        """tests if instance is a subclass of Rectangle"""
        clss = self.square.__class__
        self.assertTrue(issubclass(clss, Rectangle))

    def test_is_subclass_of_base(self):
        """tests if instance is a subclass of Base"""
        clss = self.square.__class__
        self.assertTrue(issubclass(clss, Base))

    def test_is_instance_of_square(self):
        """tests if instance is of Square class"""
        self.assertTrue(isinstance(self.square, Square))

    def test_is_instance_of_rectangle(self):
        """test if instance is of Rectangle class"""
        self.assertTrue(isinstance(self.square, Rectangle))

    def test_is_instance_of_base(self):
        """tests if instance is of Base class"""
        self.assertTrue(isinstance(self.square, Base))

    def test_id_is_number_of_instances_no_args(self):
        """tests if id is equal to instances count of Base class"""
        Base._Base__nb_objects = 0
        s = Square(2)

        i = Base._Base__nb_objects
        self.assertEqual(s.id, i)

    def test_id_increment_from_Base(self):
        Base._Base__nb_objects = 98
        s = Square(4)

        self.assertEqual(s.id, 99)

    #-------------arguments_passing----------------------
    def test_init_no_args(self):
        """tests whether error is raised if no arg is passed"""
        with self.assertRaises(TypeError):
            Square()

    def test_init_many_args(self):
        """tests whether error is raised if many args are passed"""
        with self.assertRaises(TypeError):
            Square(2, 3, 4, 5, 5, 6)

    def test_minus_optional_args(self):
        """tests instance without optional arguments"""
        s = Square(78)
        self.assertTrue(s)

    def test_default_args(self):
        """tests for the default rest arguments"""
        s1 = Square(5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_keyworded_arguments(self):
        """tests if keyworded args are accepted in instantiating"""
        s = Square(y=4, x=4, id=7, size=9)
        self.assertEqual(s.size, 9)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 7)

    #----------------Type_of_arguments------------------------
    def test_arguments_type(self):
        """tests if error is raised when invalid arguments are passed"""
        
        args_list = ['size', 'x', 'y', 'id']
        def_args = [2, 8, 9]
        test_vals = [(2,), True, "name", 3.14, [3, 4, 5], {3, 5}, None,
                {'value': 5}, float('-inf'), float('inf'), float('nan')]
        for arg in args_list:
            idx = args_list.index(arg)

            for test in test_vals:
                def_args_copy = def_args.copy()
                if (arg == 'id'):
                    if test == None:
                        continue
                def_args_copy.insert(idx, test)
                with self.assertRaises(TypeError):
                    Square(*def_args_copy)

    def test_neg_value_arguments(self):
        """Tests whether negative integral value arguments are invalid"""

        args_list = ['size', 'x', 'y', 'id']
        def_args = [2, 6, 3]
        test_val = -2
        for arg in args_list:
            idx = args_list.index(arg)
            def_args_copy = def_args.copy()
            def_args_copy.insert(idx, test_val)

            with self.assertRaises(ValueError):
                Square(*def_args_copy)

    def test_zero_value_arguments(self):
        """Tests for zero arguments on id, size parameters"""

        with self.assertRaises(ValueError):
            Square(0, 1, 3, 4)

        with self.assertRaises(ValueError):
            Square(2, 4, 0, 0)

    #------------str()----------------------
    def test_str(self):
        """Tests the __str__() function of Square class"""
        str_str = self.square.__str__()
        self.assertEqual(str_str, "[Square] (89) 2/1 - 5")

    def test_str_arg(self):
        """Tests the __str__() function with argument(s) passes"""
        with self.assertRaises(TypeError):
            self.square.__str__(4)

    def test_str_alt(self):
        """Tests the __str__() function in an alternative way"""
        self.assertEqual(str(self.square.__str__()), "[Square] (89) 2/1 - 5")

    #--------------Getters_and_setters--------------------
    def test_getter_and_setter(self):
        """Tests the getter and setter of the class Square"""

        s1 = Square(3, 4, 2, 1)
        s1.size = 57

        self.assertEqual(s1.size, 57)
        self.assertEqual(s1.width, 57)
        self.assertEqual(s1.height, 57)
        self.assertEqual(str(s1), "[Square] (1) 4/2 - 57")

    #---------------update--------------------
    def test_update_no_args(self):
        """Tests the update function of the Rectangle class"""
        sq_dict = str(self.square.__dict__)
        self.square.update()
        self.assertEqual(str(self.square.__dict__), sq_dict)

    def test_update_args(self):
        """Tests the update function with args provided"""

        s = Square(2, 4, 0, 1)
        l = s.size
        x = s.x
        y = s.y
        i = s.id
        s_dict = str(s.__dict__)

        s.update(3, 5, 1, 3)

        self.assertNotEqual(s.width, l)
        self.assertTrue(s.width == s.height)
        self.assertEqual(s.size, s.width)
        self.assertEqual(s.size, 5)
        self.assertNotEqual(s.x, x)
        self.assertEqual(s.x, 1)
        self.assertNotEqual(s.y, y)
        self.assertEqual(s.y, 3)
        self.assertNotEqual(s.id, i)
        self.assertEqual(s.id, 3)
        self.assertNotEqual(str(s.__dict__), s_dict)

    def test_update_kwargs(self):
        """Tests the update function with keyword args"""
        sq = Square(8, 9, 7, 3)
        s = sq.size
        x = sq.x
        y = sq.y
        i = sq.id
        sq.dict = str(sq.__dict__)

        sq.update(x=2, y=1, id=1, size=21)

        self.assertNotEqual(sq.size, s)
        self.assertEqual(sq.size, sq.width)
        self.assertEqual(sq.size, sq.height)
        self.assertEqual(sq.width, sq.height)
        self.assertNotEqual(sq.x, x)
        self.assertEqual(sq.x, 2)
        self.assertNotEqual(sq.y, y)
        self.assertEqual(sq.y, 1)
        self.assertNotEqual(sq.id, i)
        self.assertEqual(sq.id,1)
        self.assertNotEqual(str(sq.__dict__), sq.dict)
        
        sq.update(y=4, size=3)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.size, 3)

        sq.update(size=1)
        self.assertEqual(sq.size, sq.width, 1)
    
    def test_update_type_errors(self):
        """Tests if update function raises errors for invalid args"""
        
        s = Square(2, 3, 4, 5)
        args_list = ['id', 'size', 'x', 'y']
        def_args = [2, 8, 9]
        test_vals = [(2,), True, "name", 3.14, [3, 4, 5], {3, 5}, None,
                {'value': 5}, float('-inf'), float('inf'), float('nan')]
        for arg in args_list:
            idx = args_list.index(arg)

            for test in test_vals:
                def_args_copy = def_args.copy()
                if (arg == 'id'):
                    if test == None:
                        continue
                def_args_copy.insert(idx, test)
                with self.assertRaises(TypeError):
                    s.update(*def_args_copy)

    def test_neg_value_update(self):
        """Tests whether updated with negatives raises errors"""

        s = Square(3, 4, 5, 7)
        args_list = ['size', 'x', 'y']
        def_args = [2, 6, 1]
        test_val = -2
        for arg in args_list:
            idx = args_list.index(arg)
            def_args_copy = def_args.copy()
            def_args_copy.insert(idx, test_val)

            with self.assertRaises(ValueError):
                s.update(*def_args_copy)

    def test_zero_value_update(self):
        """Tests for zero update on id, width and height parameters"""

        s = Square(4, 5, 6, 7)
        with self.assertRaises(ValueError):
            s.update(0, 1, 3, 4)

        with self.assertRaises(ValueError):
            s.update(2, 0, 4, 0)

    def test_update_many_args(self):
        """Tests the update function if many args are passed"""
        s = Square(3, 6, 7, 3)
        s.update(3, 5, 6, 3, 6, 7, 8, 2)
        self.assertTrue(s)

    #---------------to_dictionary----------------
    def test_to_dictionary(self):
        """Tests the to_dictionary() method"""
        s = Square(3, 4, 5, 89)
        self.assertEqual(s.to_dictionary(), {'id': 89, 'size': 3, 'x': 4, 'y': 5})

    def test_to_dictionary_args(self):
        """Tests whether error is raised when args passed"""
        s = Square(3, 2, 1, 89)
        with self.assertRaises(TypeError):
            s.to_dictionary(2)

    def test_to_dictionary_type(self):
        """Tests for the type of to_dictionary()"""
        s = Square(3, 2, 4, 97)
        self.assertTrue(type(s.to_dictionary()) is dict)
