#!/usr/bin/python3
"""
This script takes one arg and
displays all values in the states
where `name` matches the argument


script is safe from ySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    get the states from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
