#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows from the 'states' table
where the name starts with the letter 'N'. The results are ordered by the 'id' column
in ascending order and printed to the standard output.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username:   The username to connect to the MySQL server.
    mysql_password:   The password for the given MySQL username.
    database_name:    The name of the database to use.

Requirements:
    - MySQLdb module must be installed.
    - The script must be run with exactly three arguments.

Example:
    ./1-filter_states.py root root_password hbtn_0e_0_usa

Note:
    The script uses a simple SQL query with a LIKE clause to filter state names
    starting with 'N'. The connection is closed after the operation.
"""

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
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    lines = cur.fetchall()
    for i in lines:
        print(i)
    cur.close()
    db.close()

