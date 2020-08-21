import sqlite3

from libs.db.dba import getConn

def select_1():
    conn = getConn()
    cur = conn.cursor()

    cur.execute('select * from test')
    rs = cur.fetchall()

    for i in rs:
        print(i)

    # conn.commit()
    conn.close()

def select_2():
    conn = getConn()
    cur = conn.cursor()

    cur.execute('select * from test where kor > 50')
    rs = cur.fetchmany(3)
    # rs = cur.fetchall()

    for i in rs:
        print(i)

    # conn.commit()
    conn.close()

def select_3(name):
    conn = getConn()
    cur = conn.cursor()

    cur.execute('select * from test where name = ?', (name, ))
    rs = cur.fetchmany(3)
    # rs = cur.fetchall()

    for i in rs:
        print(i)

    conn.close()

def update_1():
    conn = getConn()
    cur = conn.cursor()

    upt_sql = 'update test set name = "홍홍홍" where name = "홍길동"'
    cur.execute(upt_sql)
    # rs = cur.fetchmany(3)

    conn.commit()
    conn.close()

def update_0(o_name, n_name):
    conn = getConn()
    cur = conn.cursor()

    upt_sql = 'update test set name = ? where name = ?'
    cur.execute(upt_sql, (n_name, o_name))
    # rs = cur.fetchmany(3)

    conn.commit()
    conn.close()

def delete_1():
    conn = getConn()
    cur = conn.cursor()

    del_sql = 'delete from test where kor <= ?'
    cur.execute(del_sql, (80,))
    # rs = cur.fetchmany(3)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    # select_1()
    # select_2()
    # str = input('name : ')
    # select_3(str)
    # update_1()
    # update_0("홍홍홍", "홍길동""")
    delete_1()