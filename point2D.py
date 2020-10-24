import math

class point2D:

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
        print('La distancia del punto al origen es {}'.format(math.sqrt(self.x ** 2 + self.y ** 2)))

