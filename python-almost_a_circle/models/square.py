#!/usr/bin/python3
"""Defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.width = value
        self.height = value

    def __str__(self):
        """returns the str() reprensentation of square"""
        str_id = "[Square] ({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)

        return str_id + str_x_y + str_size

    def update(self, *args, **kwargs):
        if args and len(args) is not 0:
            list_attributes = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, list_attributes[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
