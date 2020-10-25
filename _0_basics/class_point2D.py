import math
""" Example of a simple class

    Usage: from class_point2D import Point2D
"""


class Point2D:

    def __init__(self, x=None, y=None):
        if x is None:
            self.x = 0.0
        else:
            self.x = x
        if y is None:
            self.y = 1.0
        else:
            self.y = y

    def print_distance(self):
        print('Distance to the origin is: {}'.format(math.sqrt(self.x ** 2 + self.y ** 2)))

