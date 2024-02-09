#!/usr/bin/python3

"""Creates an class Rectangle"""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing size.
        Args :
            width: width of rectangle.
            height: height of rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns current width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns current height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with #."""
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += "#"
            rectangle += "\n"
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """Prints the string representation of rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when the rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If either rect_1 or rect_2 isn't a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_2.area() >= rect_1.area():
            return rect_2
        elif rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a rectangle with equal width and height

        Args:
            size (int): height and width of rectangle.
        """
        return cls(size, size)
