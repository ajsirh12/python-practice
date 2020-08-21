import sqlite3
from libs.db.dba import getConn

class ManageFIle:
    def readfile(self, title):
        file = open(title, 'r', encoding='utf-8')
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

    def selectDB(self):
        conn = getConn()
        cur = conn.cursor()
        sel_sql = 'select item.name, item.price, sales.amount from item, sales where item.name = sales.name order by item.name'
        cur.execute(sel_sql)
        rs = cur.fetchall()

        conn.close()

        return rs

    def totalPrice(self, db):
        total = 0
        for i in db:
            price = i[1] * i[2]
            total += price
        return total

def main():
    mgfile = ManageFIle()

    db = mgfile.selectDB()
    money = mgfile.totalPrice(db)
    print('''
======================================================
             온라인 매출 현황
======================================================
        ''')
    print('{0:>2} {1:>10} {2:>10} {3:>10} {4:>10}'.format('', '상품명', '단가', '개수', '금액'))
    print('------------------------------------------------------')
    for i, v in enumerate(db):
        print('{0:>2} {1:>10} {2:>10} {3:>10} {4:>10}'.format(i + 1, v[0], v[1], v[2], v[1] * v[2]))
    print('------------------------------------------------------')
    print('매출 합계   ', money)
    print('======================================================')

if __name__ == '__main__':
    main()
