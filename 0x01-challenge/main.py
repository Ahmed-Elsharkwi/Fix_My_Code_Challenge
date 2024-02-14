#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    try:
        from square import Square

        s = Square(width=30, height=30)
        a = s.area_of_my_square()
        if a != (30 * 30):
            print("Wrong area_of_my_square for 30/30: {}".format(a))
            exit(1)

        s = Square(width=30, height=40)
        a = s.area_of_my_square()
        if a != (30 * 40):
            print("Wrong area_of_my_square for 30/40: {}".format(a))
            exit(1)
        
        print("OK", end="")
    except:
        print("Error: {}".format(sys.exc_info()))
