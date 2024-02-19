#!/usr/bin/python3
"""Defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the square class"""
    def __init__(self ,size, x=0, y=0, id=None):
        """Initialize instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns the str() reprensentation of square"""
        str_id = "[Square] ({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)

        return str_id + str_x_y + str_size