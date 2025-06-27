#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa with their state name,
sorted by cities.id ascending.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute(
        """SELECT cities.name FROM cities JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (state,)
        )
    rows = cur.fetchall()
    print(", ".join(row[0]for row in rows))
    cur.close()
    db.close()
