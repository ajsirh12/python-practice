# f = open('d:/python/number.txt', 'w')
# for i in range(10):
#     f.write('%d번째\n' %i)
# f.close()

# f = open('d:/python/number.txt', 'r')
#
# while True:
#     t = f.readline()
#     if t:
#         print(t, end='')
#     else:
#         break
# f.close()

# f = open('d:/python/number.txt', 'r')
#
# t = f.readlines()
# f.close()
# print(t)
#
# for i in t:
#     print(i, end='')

# f = open('d:/python/number.txt', 'r')
# t = f.read()
# c = open('d:/python/number_bak.txt', 'w')
# c.write(t)
# c.close()
# f.close()
# print(t)

# # number.txt를 읽어서 줄번호를 붙이시오.
# f = open('d:/python/number.txt', 'r')
# b = open('d:/python/number_idx.txt', 'w')
# num = 1
#
# while True:
#     txt = f.readline()
#     if txt:
#         b.write('No. ' + str(num) + ' : ' + txt)
#         num += 1
#     else:
#         break
#
# b.close()
# f.close()




