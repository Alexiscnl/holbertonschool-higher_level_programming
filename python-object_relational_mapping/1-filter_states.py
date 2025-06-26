#!/usr/bin/python3
"""Lists all states with a name starting with N
from the database hbtn_0e_0_usa."""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    lines = cur.fetchall()
    for i in lines:
        print(i)
    cur.close()
    db.close()
