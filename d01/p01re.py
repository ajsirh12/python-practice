# li = [1,2,3]
# a,b,c = map(int, li)
# print(a+b+c)

# a=(1,2,3)
# print(a, sum(a), type(a))
#
# a=[1,2,3]
# print(a, sum(a), type(a))
#
# a={1,2,3}
# print(a, sum(a), type(a))
#
# a={1:1, 2:2, 3:5}
# print(a, sum(a.values()), type(a))
#
# a=['ac', 'bb']
# a=dict(a)
# print(a)

a=[3,4,2,5,1]
print(a, type(a))
a=tuple(a)
print(a, type(a))
a=set(a)
print(a, type(a))
a=list(a)
a+=[1]
print(a, type(a))
a=set(a)
print(a, type(a))