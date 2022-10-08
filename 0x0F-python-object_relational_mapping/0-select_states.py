#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the db and get the states
    from  db.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    current = db.cursor()
    current.execute("SELECT * FROM states")
    rows = current.fetchall()

    for row in rows:
        print(row)
