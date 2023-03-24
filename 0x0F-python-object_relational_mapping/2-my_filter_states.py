#!/usr/bin/python3
"""Select state name from database hbtn_0e_0-usa that matches
user input from command line"""
import MySQLdb
import sys


if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name LIKE '{:s}' ORDER BY id \
            ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
