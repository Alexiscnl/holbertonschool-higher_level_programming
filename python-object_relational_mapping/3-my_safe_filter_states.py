#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
This version uses a parameterized query to prevent SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    states_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (states_name, ))
    lines = cur.fetchall()
    for i in lines:
        print(i)
    cur.close()
    db.close()
