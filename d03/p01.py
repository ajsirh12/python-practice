# g_a = 1
# g_b = 'symbol'
#
# def f():
#     '''This is Function'''
#     l_a = 2
#     l_b = 'qwe'
#     print(locals())
# print(f.__doc__)
#
# for i in range(3):
#     g_c = 3
#     g_d = 'asd'
#     print(id(g_c))
#     print(locals())
#
# f()
# print(globals())
#
# print(f.__dict__)
#
# class MyClass:
#     x = 10
#     y = 20
#
#     # def qwe(x, y):
#     #     print(x+y)
# MyClass.x = 50
# MyClass.z = 5
# print(MyClass.__dict__)
#
# # MyClass.qwe(2,3)
#
# import math
# print(math.pi)


# import sys
#
# x = object()
# print(sys.getrefcount(x))
#
# y = x
# print(sys.getrefcount(x))
#
# del x
# print(sys.getrefcount(y))


# i1 = 10
# i2 = 10
# print(hex(id(i1)), hex(id(i2)), i1 is i2)
#
# l1 = [1,2,3]
# l2 = [1,2,3]
# print(hex(id(l1)), hex(id(l2)), l1 is l2)
#
# s1 = 'Hello'
# s2 = 'Hello'
# print(hex(id(s1)), hex(id(s2)), s1 is s2)
#
# a = [1,[2,3,4]]
# b = a
# print(id(a), id(b))
#
# a[0] = 100
# print(a, b)
#
# import copy
# b = copy.copy(a)
# print(id(a), id(b))
#
# a[0] = 50
# print(a, b)
#
# b = copy.deepcopy(a)
# a[0] = 100
# a[1][0] = 20
# print(a, b)
# print(id(a[1]), id(b[1]))


# a = 1
# b = a
#
# a = [1, 2, 3]
# b = [4, 5, a]
# x = [a, b, 100]
# y = x
#
# print(x)
# print(y)


# def get():
#     return 1,2,3
#
# a,b,c = get()
# print(a, b, c)


# def f(t):
#     t = 20
# a = 10
# f(a)
# print(a)
#
# def h(t):
#     t = (10, 20,30)
# a = (1,2,3)
# h(a)
# print(a)
#
# def g(t):
#     t[0] = 0
# a = [1,2,3]
# g(a)
# print(a)


# # g = 1
# def f(a):
#     global g
#     g = 3
#     return a + g
#
# print(f(10))
# print(g)


# print(dir())
# print(dir(str))


# def incr(a, step=1):
#     return a + step
#
# print(incr(10))
# print(incr(10,2))


# def varg(a, *arg):
#     print(a, arg)
#
# varg(1)
# varg(1,2)
# varg(1,2,3,4,5)


# def f(width, height, **kw):
#     print(width, height)
#     print(kw)
#
# f(10, 20, depth = 10, dimension = 3)
#
# def g(a, b, *args, **kw):
#     print(a,b)
#     print(args)
#     print(kw)
#
# g(10,20,30,40,50,c=60,d=70)

# x = 100
# def A(): # outter function
#     x = 10
#     def B(): # inner function
#         global x
#         # nonlocal x
#         x = 20
#     B()
#     print(x)
# A()
# print(x)


# def func():
#     print('func')
#
# x = func
#
# print(x)
# x()


# states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']
#
# def clean_str(strs):
#     results = []
#     for s in strs:
#         s = s.strip()
#         # s = re.sub('[!#?]', '', s)
#         s = s.title()
#         results.append(s)
#     return results
#
# print(clean_str(states))


# def cold():
#     print('cold')
# def hot():
#     print('hot')
#
# def aircon(*action):
#     # action()
#     for f in action:
#         f()
#
# aircon(cold, hot)
# # aircon(hot)


# def adder(a):
#     return a + 1000

# adder = lambda a: a +1000
# print(adder(4))
#
# print((lambda  a : a + 1000)(5))


# def ad(x):
#     return x*2
#
# st = '1234'
# li = list(st)
#
# m = map(lambda a: a * 2, li)
# li = list(m)
#
# print(li)


# li = [i for i in range(10)]
# print(li)
# # l2 = list(map(lambda a : a+2 if a%2==0 else a, li))
# l2 = list(map(lambda a : a+2 if a%2==0 else str(a) if a%2==1 else a , li))
# print(l2)


# strings = ['foo', 'card', 'bar', 'abab', 'aaaa', 'abab', 'foo']
#
# strings.sort(key=lambda x: len(x))
# print(strings)
#
# strings.sort(key=lambda x: strings.count(x))
# print(strings)


# def f(x):
#     return x>=5 and x<=7
#
# li = [1,2,3,4,5,6,7,8,9,10]
# # print(list(filter(f, li)))
# print(list(filter(lambda x : x>=5 and x<=7, li)))


# def outer_f():
#     msg = 'string'
#     def inner_f():
#         print(msg)
#     return inner_f()
#
# outer_f()

# def outer_f(ttt):
#     tag = ttt
#     def inner_f(txt):
#         text = txt
#         print('<{0}>{1}</{0}>'.format(tag, text))
#     return inner_f
#
# ff = outer_f('html')
# ff('Hello World')

# help(print)

# gg = outer_f('car')
# gg('gas')


# class MyString:
#     pass
#
# s = MyString()
# print(type(s))
# print(MyString.__bases__)
#
# s2 = str()
# print(type(s2))
# print(str.__bases__)


# class Person:
#     name = '' # 클래스 변수
#
#     def chgName(self, name):
#         Person.name = name
#
#     def display(self):  #인스턴스 함수
#         self.age = 30   #self 인스턴스
#         print(Person.name, self.age)
#
# ob1 = Person()
# ob1.chgName('qwerty')
# ob1.display()
#
# ob2 = Person()
# ob2.chgName('power')
# ob2.display()


class Person:
    def __init__(self, name, age, ee = 2.0):  # 생성자
        self.name = name
        self.age = age  # self 인스턴스
        self.__eye = ee

    def display(self):  #인스턴스 함수
        print(self.name, self.age, self.__eye)

    def get_eye(self):
        return self.__eye

    def set_eye(self, ee):
        self.__eye = ee

ob1 = Person('Hong', 10, 3.0)
# ob1.eye = 1.0
ob1.set_eye(4.0)
print(ob1.get_eye())
ob2 = Person('song', 14)

li = list()
li.append(ob1)
li.append(ob2)
# li[0].display()
for i in li:
    i.display()