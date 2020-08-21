# class ManageFIle:
#     def readfile(self, title):
#         file = open(item, 'r', encoding='utf-8')
#     num = 0
#     li = []
#
#     while True:
#         txt = file.readline()
#         num += 1
#
#         if num < 3:
#             continue
#         if txt:
#             li.append(txt.split())
#         else:
#             break
#     file.close()
#
#     return li

import sqlite3

from libs.db.dba import getConn

def readfile(item):
    file = open(item, 'r', encoding='utf-8')
    num = 0
    li = []

    while True:
        txt = file.readline()
        num += 1

        if num < 3:
            continue
        if txt:
            li.append(txt.split())
        else:
            break
    file.close()

    return li

def create_table():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
    create table item(name text, price int)
    ''')
    cur.execute('''
    create table sales(name text, amount int)
    ''')

    conn.commit()
    conn.close()

def insertDB(title, name, price):
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into {} values(?, ?)'.format(title)
    cur.execute(ins_sql, (name, price))

    conn.commit()
    conn.close()

def insertDBData(name, title):
    for i in title:
        insertDB(name, i[0], i[1])

def selectDB():
    conn = getConn()
    cur = conn.cursor()
    sel_sql = 'select item.name, item.price, sales.amount from item, sales where item.name = sales.name order by item.name'
    cur.execute(sel_sql)
    rs = cur.fetchall()

    conn.close()

    return rs

def totalPrice(db):
    total = 0
    for i in db:
        price = i[1]*i[2]
        total += price
    return total


if __name__ == '__main__':
    # create_table()
    #
    # itemroute = 'd:/python/data/item.txt'
    # salesroute = 'd:/python/data/sales.txt'
    #
    # item = readfile(itemroute)
    # sales = readfile(salesroute)
    #
    # insertDBData('item', item)
    # insertDBData('sales', sales)

    db = selectDB()
    money = totalPrice(db)
    print('''
======================================================
             온라인 매출 현황
======================================================
    ''')
    print('{0:>2} {1:>10} {2:>10} {3:>10} {4:>10}'.format('', '상품명', '단가', '개수', '금액'))
    print('------------------------------------------------------')
    for i, v in enumerate(db):
        print('{0:>2} {1:>10} {2:>10} {3:>10} {4:>10}'.format(i+1, v[0], v[1], v[2], v[1]*v[2]))
    print('------------------------------------------------------')
    print('매출 합계   ', money)
    print('======================================================')


