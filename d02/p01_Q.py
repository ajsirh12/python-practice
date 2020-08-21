#Q1
a = []
num = int(input('Input Number : '))
for i in range(2):
    a.append([])

for i in range(len(a)):
    for j in range(3):
        a[i].append([num])
        num += 1
    print(a[i])

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# =====================================================================================

# #Q2
# li = []
# num = 0
#
# for i in range(1,6):
#     num = int(input('정수를 입력 [{}/5]: '.format(i)))
#     if num == 0:
#         break
#     li.append(num)
#     print(li)


# # while
# li = []
# num = 0
# i = 0
# while True:
#     i += 1
#     num = int(input('정수를 입력 [{}]: '.format(i)))
#     if num == 0:
#         break
#     li.append(num)
#     print(li)


# =====================================================================================

# #Q3
# pwd = 'password is 1234'
# print(pwd)
# pwd = pwd.replace(pwd, 'password is 5678')
# print('수정 후 : ' + pwd)
#
# notice = '매우 많은 환자가 발생합니다.'
# print(notice)
# notice = notice.replace(notice, '항상 많은 코로나 환자가 발생합니다.')
# print('수정 후 : ' + notice)

# =====================================================================================

# #4
# url = 'http://www.naver.com/news/today=20200131'
# user = 'name:홍길동 age:22 sex:남자 nation:대한민국'
#
# url = url.split('/')
# for i in url:
#     if i == '':
#         url.remove(i)
# print(url)
#
# user = user.split()
# userInfo = dict()
# for i in user:
#     info = i.split(':')
#     userInfo.update({info[0]:info[1]})
#
# for key, val in userInfo.items():
#     print('{0} -> {1}'.format(key, val))

# =====================================================================================

# #5
# space= ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성','지구']
# for num, i in enumerate(space):
#     if i == '지구':
#         space[num] = i.replace(i, 'earth')
# print(space)

# =====================================================================================

# #6
# covid = {'January':4500, 'February':5000, 'March':2500, 'April':1200,
# 'May':567, 'June':434, 'July':323}
#
# total = 0
# avg = 0
# for key, val in covid.items():
#     total += val
# avg = total / len(covid)
#
# print(covid.values())
# print('환자수 총계: {}'.format(total))
# print('환자수 평균: {}'.format(avg))


