#!/usr/bin/python3
"""Select state name matching argument while preventing SQL Injection"""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id",
                (sys.argv[4],))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
