import sqlite3
from libs.db.dba import getConn

def create_table():
    conn = getConn()    # DB 접속 정보
    cur = conn.cursor() #
    cur.execute('''
    create table test(name text, kor int, eng int, math int)
    ''')
    conn.commit()   # 완전히 반영
    conn.close()

if __name__ == '__main__':
    create_table()

    
