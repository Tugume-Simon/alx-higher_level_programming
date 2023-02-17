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

    # --------------to_json_string----------------------
    def test_to_json_string_proper(self):
        """Tests the to_json_string method with right arguments"""
        r = Rectangle(4, 5, 1, 2, 89)
        s = Square(3, 4, 1, 67)

        self.assertEqual(Base.to_json_string([{'height': 3}, {'width': 3}]),
                         '[{"height": 3}, {"width": 3}]')

        dicts = list([r.to_dictionary(), s.to_dictionary()])
        self.assertEqual(Base.to_json_string(dicts),
                         '''[{"id": 89, "width": 4, "height": 5, "x": 1,\
 "y": 2}, {"id": 67, "size": 3, "x": 4, "y": 1}]''')

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
        """Tests whether an empty list is returned when empty list passed"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_many_arguments(self):
        """Tests whether error is raised if many arguments are passed"""
        with self.assertRaises(TypeError):
            Base.to_json_string([{'name': True}, {'age': 8}], [])

    # -------------------save_to_file-------------------
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

    def test_save_to_file_type_list_of_not_objects(self):
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

    def test_save_to_file_list_of_invalid_objects(self):
        """Test whether non-Base instances are allowed"""
        class Testclass:
            def __init__(self):
                self.test = True

            def out(self):
                print("test")

        test_obj1 = Testclass()
        test_obj2 = Testclass()

        self.assertFalse(isinstance(test_obj1, Base))
        with self.assertRaises(TypeError):
            Base.save_to_file([test_obj1, test_obj2])

    def find(self, name, path):
        """Searches for a file named 'name' in 'path'

        The file is searched using os.walk function which
        yields a 3-tuple

        - dirpath is a string, the path to the directory.
        - dirnames is a list of the names of the subdirectories in dirpath
        (excluding '.' and '..').
        - filenames is a list of non-directory filenames in dirpath.

        Returns: raises an Exception if file was not found
        """
        search = ""
        for dirpath, dirnames, filenames in os.walk(path):
            if name in filenames:
                search = os.path.join(dirpath, path)

        if len(search) == 0:
            raise Exception("file not found")

        return search

    def test_save_to_file_created(self):
        """Tests if a file is created

        if the file exists, it is deleted and then the call to
        save_to_file() is made. The search is made for the file.
        if it exists, then it was created, if not, then save_to_file()
        failed
        """

        r = Rectangle(5, 4, 3, 2, 1)

        filename = r.__class__.__name__ + '.json'  # Rectangle.json
        try:
            with open(filename, 'r') as f:
                f.readline()
        except (OSError, FileNotFoundError):
            pass
        else:
            os.remove(f'./{filename}')

        Rectangle.save_to_file([r])
        self.assertTrue(self.find(filename, "./"))

    def test_save_to_file_verify_content(self):
        """Tests if the right json content is writen to file

        If the content is not in JSON format, then the json.load()
        method will fail and will raise an exception
        """

        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        expected_write = '''[{"id": 1, "size": 1, "x": 1, "y": 1},\
 {"id": 2, "size": 2, "x": 2, "y": 2}]'''

        filename = s1.__class__.__name__ + '.json'  # Square.json
        Square.save_to_file([s1, s2])

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.readline()

        self.assertEqual(content, expected_write)

    def test_save_to_file_verify_json(self):
        """Tests whether the content writted to file is in json format"""

        r1 = Rectangle(2, 3, 1, 1, 1)
        r2 = Rectangle(102, 43, 23, 455, 32)
        filename = r1.__class__.__name__ + '.json'  # Rectangle.json

        write = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])

        with open(filename, 'r', encoding='utf-8') as f:
            saved = json.load(f)

        self.assertEqual(write, saved)

    # -------------------from_json_string----------------------
    def test_from_json_string_no_args(self):
        """Tests the from_json_to_string() method when no argument is passes"""

        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_many_args(self):
        """Tests the from_json_to_string() method with many args passed"""

        string1 = '{"Square": 2, "Rectangle": 1}'
        string2 = '[3, 4, 5]'

        with self.assertRaises(TypeError):
            Base.from_json_string(string1, string2)

    def test_from_json_string_type(self):
        """Tests from_json_to_string() mehtod with non-string types"""

        non_string_types = [1, 1.34, [1, 2, 3], (2,), {'side': 3, 'up': 3},
                            True, {2, 3}]

        for test in non_string_types:
            with self.assertRaises(TypeError):
                Base.from_json_string(test)

    def test_from_json_string_empty(self):
        """Tests from_json_string() method with Nonetype and empty string"""

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_output(self):
        """Tests for correct output of from_json_string()"""

        str1 = '[1, 2, 3]'
        str2 = '[{"Square": 2, "Rectangle": 3}]'
        str3 = '3'
        str4 = '4.45'

        self.assertEqual(Base.from_json_string(str1), [1, 2, 3])
        self.assertEqual(Base.from_json_string(str2),
                         [{'Square': 2, 'Rectangle': 3}])
        self.assertEqual(Base.from_json_string(str3), 3)
        self.assertEqual(Base.from_json_string(str4), 4.45)

    def test_from_json_string_non_json_strings(self):
        """Tests whether an exception is raised for non-json strings"""

        strings = ["string", '(3, 4)', '"class": 3, "grade": 4']
        for string in strings:
            with self.assertRaises(ValueError):
                Base.from_json_string(string)

    # ---------------create----------------------
    def test_create_no_args(self):
        """Tests call to create without arguments"""
        with self.assertRaises(ValueError):
            Rectangle.create()

    def test_create_non_kwargs(self):
        """Tests create function with non keyworded arguments"""

        args = [2, "stg", [2, 3, 4], {3, 4}]
        for arg in args:
            with self.assertRaises(TypeError):
                Square.create(arg)

        with self.assertRaises(TypeError):
            Square.create(args)

    def test_create_output(self):
        """Tests for right output of the create() method"""
        new = Square.create(size=5, x=3, y=2, id=89)
        self.assertTrue(new)
        self.assertTrue(type(new) is Square)
        self.assertTrue(isinstance(new, Base))
        self.assertEqual(new.to_dictionary(), {'id': 89, 'size': 5, 'x': 3,
                         'y': 2})

        sq = Square.create(**new.to_dictionary())
        self.assertEqual(sq.to_dictionary(), {'id': 89, 'size': 5, 'x': 3,
                         'y': 2})
        self.assertNotEqual(sq, new)

    # ----------------load_from_file-------------------------
    def test_load_from_file_args(self):
        """Tests if an exception is raised if arguments are passed"""
        with self.assertRaises(TypeError):
            Square.load_from_file(3)

    def test_load_from_file_non_existent(self):
        """Tests if the function raises exception if the file doesn't exist"""
        filename = 'Rectangle.json'

        try:
            with open(filename, 'r') as f:
                f.readline()
        except (OSError, FileNotFoundError):
            pass
        else:
            os.remove(f'./{filename}')

        with self.assertRaises(FileNotFoundError):
            Rectangle.load_from_file()

    def test_load_from_file_empty(self):
        """Tests if an empty list is returned if the file is empty"""

        filename = 'Square.json'

        with open(filename, 'w') as f:
            f.write('')

        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_valid(self):
        """Tests whether objects are created from json files

        First some rectangle and square data is written to the
        corresponding files as json
        """
        data_sq1 = {'id': 997, 'size': 6, 'x': 1, 'y': 1}
        data_sq2 = {'id': 65, 'size': 9, 'x': 12, 'y': 8}

        data_rect1 = {'id': 873, 'width': 78, 'height': 35, 'x': 0, 'y': 1}
        data_rect2 = {'id': 1024, 'width': 83, 'height': 88, 'x': 1, 'y': 23}

        s1 = Square(id=997, size=6, x=1, y=1)
        s2 = Square(id=65, size=9, x=12, y=8)

        r1 = Rectangle(id=873, width=78, height=35, x=0, y=1)
        r2 = Rectangle(id=1024, width=83, height=88, x=1, y=23)

        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        rect_objs = Rectangle.load_from_file()
        sq_objs = Square.load_from_file()

        for instance in rect_objs:
            self.assertTrue(type(instance) is Rectangle)

        for instance in sq_objs:
            self.assertTrue(type(instance) is Square)

        self.assertEqual(rect_objs[0].to_dictionary(), data_rect1)
        self.assertEqual(rect_objs[1].to_dictionary(), data_rect2)

        self.assertEqual(sq_objs[0].to_dictionary(), data_sq1)
        self.assertEqual(sq_objs[1].to_dictionary(), data_sq2)
