#!/usr/bin/python3
"""
    Create Conexion to mysql server and execute a SELECT request
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute('SELECT * FROM states ORDER BY id;')
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
