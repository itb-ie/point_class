class Point(object):

    def __init__(self, provided_x=0, provided_y=0, color="blue"):
        self.x = provided_x
        self.y = provided_y
        self.color = color
        # always returns None !!

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x=0):
        self.x = x

    def set_y(self, y=0):
        self.y = y

    def __str__(self):
        return "<{},{}> colored {}".format(self.x, self.y, self.color)
        # the same exact thig as: return "<" + str(self.x) + "," + str(self.y) + ">"

    def __repr__(self):
        # this is when you want to print a list of points
        return "<{},{}>".format(self.x, self.y)

    def distance(self, other=None):
        if other is None:
            other = Point(0,0)
        x = self.x - other.x #-3 -> 9
        y = self.y - other.y # -4 -> 16
        return (x**2 + y**2)**0.5

    #overload + sign
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # overload the ==
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    # overload the <
    def __lt__(self, other):
        #compare the distance to origin for both self and other
        return self.distance() < other.distance()


p = Point(1, 2, "red")
print(p)

p2 = Point(4)
p2.set_y(6)
print(p2)

#create a a list of points
lp = [p, p2]
print(lp)
p3 = p + p2
print(p3)
p4 = Point(5, 8)
print(p3 == p4)
print(p3 < p4)
lp.append(p3)
lp.append(p4)
lp.append(Point(1, 0, "yellow"))
# the cool part is that because I have __lt__ and __eq__ I can now sort the list
lp.sort()
print(lp)


