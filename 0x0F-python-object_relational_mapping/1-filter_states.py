#!/usr/bin/python3
"""
    Create Conexion to mysql server and execute a SELECT, LIKE, ORDER request
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()

    c.execute('SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id;')
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    conn.close()
