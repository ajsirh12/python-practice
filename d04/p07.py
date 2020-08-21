import sqlite3
from libs.db.dba import getConn

def insert_1():
    conn = getConn()
    cur = conn.cursor()

    cur.execute('''
    insert into test values('홍길동', 60, 70, 80)
    ''')

    conn.commit()
    conn.close()

def insert_2():
    conn = getConn()
    cur = conn.cursor()

    ins_sql = 'insert into test values(?, ?, ?, ?)'
    cur.execute(ins_sql, ('김철수', 55, 20, 95))

    conn.commit()
    conn.close()

def insert_3():
    conn = getConn()
    cur = conn.cursor()

    li = [('이영희', 80,55,95), ('최영희', 55,95,80), ('김영희', 95,85,55)]
    ins_sql = 'insert into test values(?, ?, ?, ?)'
    cur.executemany(ins_sql, li)

    conn.commit()
    conn.close()

def insert_0(name, kor, eng, math):
    conn = getConn()
    cur = conn.cursor()

    ins_sql = 'insert into test values(?, ?, ?, ?)'
    cur.execute(ins_sql, (name, kor, eng, math))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    # insert_1()
    # insert_2()
    # insert_3()
    insert_0('박철수', 70,80,60)