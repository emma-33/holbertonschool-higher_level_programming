#!/usr/bin/python3
"""Define a rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Represents the rectangle class"""
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """"y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints the rectangle with #"""

        if self.__width == 0 or self.__height == 0:
            print("")

        for y in range(self.__y):
            print("")

        for height in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """returns the str() reprensentation of rectangle"""
        str_id = "[Rectangle] ({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_width_height = "{}/{}".format(self.width, self.height)

        return str_id + str_x_y + str_width_height
