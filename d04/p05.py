# # xml 만들기
# from xml.etree.ElementTree import *
#
# person = Element('person')
#
# name = Element('name')
# name.text = 'Mr.Hong'
# person.append(name)
#
# age = Element('age')
# age.text = '20'
# person.append(age)
#
# SubElement(person, 'address').text = 'S.Korea'
#
# dump(person)    # print
#
# tel = Element('tel')
# tel.text = '010-1111-1111'
# person.insert(1, tel)
#
# dump(person)
#
# person.remove(tel)
#
# person.attrib['date'] = '2020-07-23'
# dump(person)
#
# ElementTree(person).write('d:/python/person.xml')


# # xml 읽기
# import xml.etree.ElementTree as EE
#
# f = EE.parse('d:/python/person.xml')
# root = f.getroot()
# print(root)
# print(root.tag)
# print(type(root))
#
# for i in root:
#     print(i.tag, i.text)


# # JSON 만들기 딕셔너리 - key : value
#
# li = [{'name':'Mr.Lee', 'KOR':60, 'ENG':70, 'MATH':80},
#       {'name':'Mr.Kim', 'KOR':50, 'ENG':50, 'MATH':50},
#       {'name':'Mr.Son', 'KOR':80, 'ENG':30, 'MATH':70},]
#
# import json
# with open('d:/python/grade.json', 'w') as f:
#     json.dump(li, f, ensure_ascii=False)


# # JSON 읽기
# import json
#
# with open('d:/python/grade.json', 'r') as f:
#     info = json.load(f)
#
# print(f, type(f))
# for i in info:
#     for k, v in i.items():
#         print(k, v)
#     print('==================')
