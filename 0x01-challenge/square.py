#!/usr/bin/python3
"""This module contains the class square"""


class Square():
    """Definations of the class square"""

    def __init__(self, *args, **kwargs):
        """ Initializer for square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        """ String format """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_mySquare())
