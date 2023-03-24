#!/usr/bin/python3
"""List all cities of the state passed as an argument"""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT name FROM cities WHERE cities.state_id=\
            (SELECT id FROM states WHERE name='{:s}')".format(sys.argv[4]))
    query_rows = cur.fetchall()

    count = 0

    for row in query_rows:
        if count > 0:
            print(", ", end="")
        print(row[0], end="")
        count += 1
    print()

    cur.close()
    conn.close()
