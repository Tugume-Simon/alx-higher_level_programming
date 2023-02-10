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

    def __str__(self):
        """String representation of square object"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
