#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa, sorted by id ascending."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        port=3306,
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    lines = cur.fetchall()
    for i in lines:
        print(i)
    cur.close()
    db.close()
