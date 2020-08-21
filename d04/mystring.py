class MyString:

    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return self.s + other

    def __mul__(self, other):
        str = self.s
        for i in range(1,other):
            str += self.s
        return str

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set__x(self, x):
        self.x = x

    def get__x(self):
        return self.x

    def set__y(self, y):
        self.y = y

    def get__y(self):
        return self.y

    def __add__(self, other):
        newx = int(self.x) + int(other.x)
        newy = int(self.y) + int(other.y)
        # return 'Point({},{})'.format(newx, newy)
        return Point(newx, newy)

    def __sub__(self, other):
        newx = int(self.x) - int(other.x)
        newy = int(self.y) - int(other.y)
        # return 'Point({},{})'.format(newx, newy)
        return Point(newx, newy)

    def dp(self):
        print('Point({0},{1})'.format(self.x, self.y))

s = MyString('Python Progarammer is Good')
t = s/' '

# p = s.__truediv__('o')
# print(p)

print(type(t))
print(t)

print(s+'Job')
print(MyString('Python')*3)

p1 = Point(100,200)
p2 = Point(50,50)
p3 = p1 + p2
p4 = p1 - p2

# print(p3)
# print(p4)
p3.dp()
p4.dp()