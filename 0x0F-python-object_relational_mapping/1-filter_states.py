#!/usr/bin/python3
"""Select all names from the database hbtn_0e_0_usa
starting with letter N"""
import MySQLdb
import sys


if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
