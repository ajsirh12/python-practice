# # 1
# for i in range(10):
#     print(i, end=' ')
# print('\n')
#
# # 2
# for i in range(1,11):
#     print(i, end=' ')
# print('\n')
#
# # 3
# for i in range(10,0,-1):
#     print(i, end=' ')
# print('\n')
#
# # 4
# # 홀수만 출력
# for i in range(1,100,2):
#     print(i, end=' ')
# print('\n')
#
# # 5
# # 1~100 홥
# total = 0
# for i in range(1,101):
#     total += i
# print(total)
# print()
#
# # 6
# # 1~100 짝수 합
# total = 0
# for i in range(1,101):
#     if i%2==0:
#         total += i
# print(total)

# # 7
# # 두 수를 입력 받아 작은수부터 큰 수까지 출력
# num = input('Input : ').split()
#
# num[0] = int(num[0])
# num[1] = int(num[1])
#
# if num[0] > num[1]:
#     for i in range(num[1], num[0]+1):
#         print(i, end=' ')
# else:
#     for i in range(num[0], num[1]+1):
#         print(i, end=' ')

# 8
# 입력된 데이터에 따라 다음과 같이 출력
# input : a d 4 -
# a-
# bc-
# dab-
# cdab-
val = input('Input : ').split()

if ord(val[0]) < ord(val[1]):
    alp = [chr(i) for i in range(ord(val[0]), ord(val[1]) + 1)]
elif ord(val[1]) < ord(val[0]):
    alp = [chr(i) for i in range(ord(val[1]), ord(val[0]) + 1)]
else:
    alp = [val[0]]

qwe = int(val[2])
idx = 0

for i in range(int(val[2])):
    for j in range(int(val[2]) - qwe + 1):
        print(alp[idx], end='')
        idx += 1
        if idx == len(alp):
            idx = 0
    qwe -= 1
    print(val[3])


