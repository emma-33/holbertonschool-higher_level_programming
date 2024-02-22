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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """returns the str() reprensentation of square"""
        str_id = "[Square] ({}) ".format(str(self.id))
        str_x_y = "{}/{} - ".format(str(self.x), str(self.y))
        str_size = "{}".format(str(self.width))

        return str_id + str_x_y + str_size

    def update(self, *args, **kwargs):
        """update method"""
        if args and len(args) != 0:
            list_attributes = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, list_attributes[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        dictionary = {"id": self.id, "size": self.size, "x": self.x,
                      "y": self.y}
        return dictionary
