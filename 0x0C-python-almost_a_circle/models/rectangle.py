#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, a subclass of Base

    Attributes:
        width (int): private, width of the rectangle
        height (int): private, height of the rectangle
        x (int): private, x-offset relative to the top left corner
        y (int): private, y-offset relative to the top left corner

    Each of these attributes have its own getter and setter

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes object attributes

        Args:
            width: width of rectangle
            height: height of rectangle
            x: offset-x
            y: offset-y
            id: object ID

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """int: width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """int: height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """int: x cordinate"""
        return self.__x

    @property
    def y(self):
        """int: y cordinate"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = int(value)

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = int(value)

    @x.setter
    def x(self, cordinate):
        """sets the x cordinate of the rectangle"""
        if type(cordinate) is not int:
            raise TypeError("x must be an integer")

        if cordinate < 0:
            raise ValueError("x must be >= 0")

        self.__x = cordinate

    @y.setter
    def y(self, cordinate):
        """sets the y cordinate of the rectangle"""
        if type(cordinate) is not int:
            raise TypeError("y must be an integer")

        if cordinate < 0:
            raise ValueError("y must be >= 0")

        self.__y = cordinate

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints a pictorial representation of the rectangle"""
        for i in range(self.y):
            print()
        for h in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the object representation in string format"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} -\
 {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """updates the attribute(s) with a new argument"""

        if len(args) > 0:
            attribs = ['id', 'width', 'height', 'x', 'y']
            for n in range(len(attribs)):
                if attribs[n] == 'id':
                    if type(args[n]) is not int:
                        raise TypeError("id must be an integer")
                    if args[n] <= 0:
                        raise ValueError("id must be > 0")
                setattr(self, attribs[n], args[n])
        else:
            for key, value in kwargs.items():
                if key == 'id' and type(value) is not int:
                    raise TypeError("id must be an integer") 
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
