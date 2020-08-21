from itertools import product

# from libs.maths.cals import *

# print(hap(10,5))
# print(mul(5,2))
# print(sub(5,10))
# print(div(3,4))
#
# print("abc" + str(1), end=' ')
# print("abc" + format(1,"d"))
#
# s = 'i like Python'
#
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())

# s = 'I Like Python. I Like Java Also'
#
# print(s.count('Like'))
#
# print(s.find('Like'))
# print(s.find('Like', 5))
# print(s.find('JS'))
# print(s.rfind('Like'))
#
# print(s.startswith('I Like'))
# print(s.startswith('I Like', 2))
# print(s.endswith('Also'))
# print(s.endswith('Java', 0, 26))
#
# print(s.index('Like'))

# s = '  spam and ham  '
#
# print(s)
# print(s.strip())
# print(s.rstrip())
# print(s.lstrip())
#
# s = '<><abc><><def><><>'
# print(s.strip('<>'))
# print(s.replace('<','').replace('>',''))
#
# s = 'Hello Java'
# print(s.replace('Java', "Python"))
#
# s = "King and Queen"
#
# print(s.center(60))
# print(s.center(60,'-'))
# print(s.ljust(60,'-'))
# print(s.rjust(60,'-'))
#
# s = 'abcdef'
# print(s[::-1])
# rs = s[::-1]
# print(rs)
#
# print(s[::2])

# s = 'spam and ham'
# t = s.split()
# print(t)
# t = s.split('and')
# print(t)
#
# s2 = ":".join(t)
# print(s2)
#
# s3 = "one:two:three:four:five"
# print(s3.split(':',2))
# print(s3.rsplit(':',2))
#
# lines = '''1st line
# 2nd line
# 3rd line
# 4th line'''
#
# print(lines.splitlines())
# print(lines.split("\n"))


# str = "<><><email><><kbs><><>"
#
# print(str)
# fullEmail = str.replace('kbs','@kbs.com').replace('<','').replace('>','')
# print(fullEmail)
#
# str2 = str.strip('<>').split('><><')
# print('@'.join(str2)+'.com')
#
# str = list(str)
# print(str, type(str))
# str = set(str)
# print(str, type(str))

# print('1234'.isdigit())
# print('abcd'.isalpha())
#
# print('1234'.isalpha())
# print('abcd'.isdigit())
#
# print('abcd'.islower())
# print('ABCD'.isupper())
#
# print('\n\n'.isspace())
# print(' '.isspace())
# print(''.isspace())
#
# print('20'.zfill(5))
# print('1234'.zfill(5))

# l = [1,2,'python']
#
# print(l[-2],l[-1],l[0],l[1],l[2])
# print(l[1:3])
# print(l*2)
# print(l+[3,4,5])
# print(len(l))
# print(2 in l)
#
# #추가
# l.append([3,4,5])
# print(type(l[3]))
#
# #찾기
# print(l.index('python'))
#
# #세기
# print(l.count('python'))
#
# #삽입
# #list.insert(index, value)
# l.insert(2,5)
# print(l)
#
# #삭제
# #del(list[index])
# del(l[0])
# print(l)
#
# #list.pop(index)
# l.pop(1)
# print(l)
#
# #list.remove(value)
# l.remove(2)
# print(l)
#
# #list.clear()
# l.clear()
# print(l)


# a = [1,6,3,24,5]
# print(sum(a))
# print(max(a))
# print(min(a))
# a.reverse()
# print(a)
#
# a.sort()
# print(a)
#
# a.sort(reverse=True)
# print(a)
#
# a.extend([6,7,8])
# print(a)

# a = [3,2,4,1,5]
#
# a.sort()
# print(a)
# b = tuple(a)
# print(b)
# c = list(b)
# print(c)
# a+=[1]
# print(a)
# a = set(a)
# a = list(a)
# print(a)


# a = [1, 12, 123, 1234]
#
# a[0:2] = [10, 20]
# print(a)
#
# a[0:2] = [10]
# print(a)
#
# a[1:2] = [20]
# print(a)
#
# a[2:3] = [30]
# print(a)

name = 'My name is'
str = 'John cena'

print(name.split())
print(name + str)
print("{} {}".format(name, str))