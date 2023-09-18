#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
""" This module lists all the states from the
    database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main():
    """
        Function containing code to select all the states
        from the database.
    """

    # Create a database connection
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="uf8mb4"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM `states` ORDER BY id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
