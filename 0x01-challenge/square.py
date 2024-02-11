#!/usr/bin/python3

class square():

    # Removed height since a square has the same width and height
    width = 0


    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        # Modified PermiterOfMySquare method to return 4 * self.width
        return (self.width * 4)

    def __str__(self):
        # Modified the str rep to return the width only "removed self.height"
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=9)
    print(s)
    # Modified that print fun to print only the width
    print(s.width)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
