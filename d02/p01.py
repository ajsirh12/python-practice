# fname = 'Hong Gil Dong'
#
# fname = fname.split()
#
# name = fname[1].lower()+fname[2].lower()+'.'
# lastname = fname[0].lower()
# addr = '@daum.net'
# print(name+lastname+addr)
#
# fname[2] = fname[2].lower()+'.'
# fname[0] = fname[0].lower()+'@daum.net'
# print(fname[1].lower()+fname[2]+fname[0])

# a = [1, 12, 123, 1234]
#
# a[1:1] = ['a']
# print(a)
#
# a[5:] = [12345]
# print(a)
#
# a[:0] = [-2, -1, 0]
# print(a)
#
# a += [777]
# print(a)
#
# a.extend([3, 5])
# print(a)
#
# a.append([999, 1000])
# print(a)
# print(a[12][0])
#
# a.insert(2,-4)
# print(a)


# a=[1,2,3]
# print(a)
# a.append(5)
# print(a)
# a.insert(3,4)
# print(a)
# print(a.count(2))
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.remove(3)
# print(a)
# a.extend([6,7,8])
# print(a)


# stack = []
#
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print(stack)
#
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)


# s = '34152'
# ls = []
#
# temp = list(s)
# temp.sort()
# temp.reverse()
# print(temp)
#
# i=0
# while i<5:
#     ls.append(temp[i])
#     i+=1
#     print(ls)
#
# while len(ls)>0:
#     ls.pop(0)
#     print(ls)
#
# # ls.append(temp[0])
# # print(ls)
# # ls.append(temp[1])
# # print(ls)
# # ls.append(temp[2])
# # print(ls)
# # ls.append(temp[3])
# # print(ls)
# # ls.append(temp[4])
# # print(ls)
# # ls.pop(0)
# # print(ls)
# # ls.pop(0)
# # print(ls)
# # ls.pop(0)
# # print(ls)
# # ls.pop(0)
# # print(ls)
# # ls.pop(0)
# # print(ls)

# l = [10, 2, 22, 9, 8, 33, 4, 11]
# l.sort(key=str)
# print(l)
#
# l.sort(key=int)
# print(l)

# import sys
#
# print(sys.argv)
# print(type(sys.argv))
#
# args = sys.argv[1:]
# print(args)
#
# a = int(args[0])
# b = int(args[2])
# c = args[1]
#
# qwe = ['+', '-', '*', '/']
#
# for e in qwe:
#     if c == e:
#         print('{0} {2} {1} = {3}'.format(a, b, c, eval(str(a) + c + str(b))))
#
# # if c == '+':
# #     print('{0} {2} {1} = {3}'.format(a, b, c, a + b))
# # elif c == '-':
# #     print('{0} {2} {1} = {3}'.format(a, b, c, a - b))
# # elif c == '*':
# #     print('{0} {2} {1} = {3}'.format(a, b, c, a * b))
# # elif c == '/':
# #     print('{0} {2} {1} = {3}'.format(a, b, c, a / b))

# a = {1,2,3,}
# print(a)
#
# a.discard(4)
# a.update({5,6,7,1})
# print(a)
#
# s = set()
# print(s)
#
# s.add(4)
# s.add(1)
# print(s)
# s.discard(2)
#
# s.update({2,3})
# s.remove(3)
# print(s)
#
# s.clear()
# print(s)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8,9}
#
# # s3 = s1.union(s2)
# s3 = s1 | s2
# print(s3)
#
# # s4 = s1.intersection(s2)
# s4 = s1 & s2
# print(s4)
#
# # s4 = s1.difference(s2)
# s4 = s1 - s2
# print(s4)
#
# # s5 = s1.symmetric_difference(s2)
# s5 = s1 ^ s2
# print(s5)
#
# print(s1.issuperset(s4))
# print(s5.issuperset(s1))
# print(s2.issubset(s3))

# t = (1,2,3,4,5,6)
# print(t, type(t))
# a, *b, c, d = t
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

# d = {'basket':5, 'soccer': 11, 'base': 9}
# print(d, type(d))
#
# print(d['basket'])
#
# d['volley'] = 6
# print(d, type(d))
#
# print(len(d))
# print('soccer' in d)
# print('volley' not in d)


# li = list(range(0,10))
# print(li)
#
# li = list(range(10,0,-1))
# print(li)
#
# li = list(range(-20, 25, 5))
# print(li)

# #리스트표현식
# li = [i for i in range(10)]
# print(li)
# li = list(i*2 for i in range(10))
# print(li)
# li = list(i*2+1 for i in range(10))
# print(li)
# li = list(i for i in range(10) if i%2 == 1 or i==2)
# print(li)
# li = list('{}*{}={}'.format(j,i,j*i) for j in range(2, 10) for i in range(1, 10))
# j = 0
# for i in li:
#     print(i)
#     j += 1
#     if(j%9==0):
#         print('\n')


# li = list(range(10, 101, 10))
# for num, value in enumerate(li):
#     print(num, value)
#
# for num, value in enumerate(range(0,100,10)):
#     print(num, value)


# li = list(range(101))
# for num, val in enumerate(li):
#     if li[num] == 0:
#         continue
#     elif li[num] % 3 == 0 and li[num] % 5 == 0:
#         print(num, 'ThreeFive')
#     elif li[num] % 3 == 0:
#         print(num, 'Three')
#     elif li[num] % 5 == 0:
#         print(num, 'Five')
#     else:
#         print(num, val)


# li = list(range(1, 101))
# for num, val in enumerate(li):
#     print(num+1, 'ThreeFIve'*(val%15==0) or 'Three'*(val%3==0) or 'Five'*(val%5==0) or val)


# a = [] #리스트 2개 생성
# num = 0
# for i in range(2):
#     a.append([])
#
# for i in range(len(a)):
#     for j in range(3):
#         a[i].append([num])
#         num += 1
#     print(a[i])
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()
#
# row = 0
# col = 0
#
# while row < len(a):
#     while col < len(a[row]):
#         print(a[row][col], end=' ')
#         col += 1
#     row += 1
#     col = 0
#     print()
#
# from pprint import pprint
# pprint(a, indent=2, width=20)

#리스트를 2차원 배열처럼
# a = [[1,2,3],[4,5,6]]
# print(a)
# print(a[0][0]) #1
# print(a[0][1]) #2
# print(a[0][2]) #3
# print(a[1][0]) #4
# print(a[1][1]) #5
# print(a[1][2]) #6


# d = dict(a=1, b=2, c=3, d=4)
# keys = d.keys()
# print(keys, type(keys))
#
# values = d.values()
# values = list(values)
# print(values, type(values))
#
# for key in keys:
#     print('{0}:{1}'.format(key, d[key]))
#
# for key, val in d.items():
#     print(key, val)


# d = dict(a=1, b=2, c=3, d=4)
#
# n = d.get('a')
# print(n)
# n = d.get('z')
# print(n)
# n = d.get('z','No')
# print(n)
# n = d.setdefault('z', '99')
# print(n)
# print(d)
# n = d.pop('a')
# print(n)
# print(d)
# n = d.popitem()
# print(n)
# print(d)
# d.update({'a':1})
# print(d)
# d.clear()
# print(d)


# seq1 = {1,2,3}
# seq2 = {5,6,7}
#
# # z = zip(seq1,seq2)
# # print(z, type(z))
# #
# # for t in z:
# #     print(t, type(t))
#
# z = zip(seq1,seq2)
# for idx, (a,b) in enumerate(z):
#     print("%d : %s, %s" %(idx, a, b))
#
# d1 = [{'q', 'w'}, ['a', 'd'], ('z','x')]
#
# seq1, seq2 = zip(*d1)
# print(seq1, type(seq1))
# print(seq2, type(seq2))


# str = ['a','as','bat','car','dove','python']
# str1 = [s for s in str if len(s) <= 2]
# print(str1, type(str1))
# str1 = list(s for s in str if len(s) <= 2)
# print(str1, type(str1))
#
# str2 = [len(s) for s in str]
# print(str2, type(str2))
#
# str3 = ['{}:{}'.format(s, len(s)) for s in str]
# print(str3, type(str3))
#
# ddc = dict()
#
# for i in str3:
#     d1, d3 = i.split(':')
#     ddc.update({d1:int(d3)})
# print(ddc, type(ddc))
#
# dd = dict(zip(str, str2))
# print(dd, type(dd))
#
# str = ['a','as','bat','car','dove','python']
# dicts = {s:len(s) for s in str}
# print(dicts)


# li = [[0 for i in range(3)] for i in range(2)]
# print(li)
#
# li = [[0]*3 for i in range(2)]
# print(li)






