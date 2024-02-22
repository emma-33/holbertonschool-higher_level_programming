#!/usr/bin/python3
"""Define a rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Represents the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
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
        if type(value) is not int:
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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            list_attributes = ['id', 'width', 'height', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, list_attributes[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        dictionary = {"id": self.id, "width": self.width,
                      "height": self.height, "x": self.x, "y": self.y}
        return dictionary
