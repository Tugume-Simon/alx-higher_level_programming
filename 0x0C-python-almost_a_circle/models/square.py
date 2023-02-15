#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, subclass of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square class

        Args:
            size (int): size of square side
            x (int): x cordinate
            y (int): y cordinate
            id (int): object ID

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the square size"""
        return self.width

    @size.setter
    def size(self, val):
        """set the size of the square side"""
        self.width = val
        self.height = val

    def __str__(self):
        """String representation of square object"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """update of square object"""

        if len(args) > 0:
            attribs = ['id', 'size', 'x', 'y']
            for n in range(len(attribs)):
                if attribs[n] == 'id':
                    if type(args[n]) is not int:
                        raise TypeError("id must be an integer")
                    if args[n] <= 0:
                        raise ValueError("id must be >= 0")
                setattr(self, attribs[n], args[n])
        else:
            for key, value in kwargs.items():
                if key == 'id' and type(value) is not int:
                    raise TypeError("id must be an integer")
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the square object"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
