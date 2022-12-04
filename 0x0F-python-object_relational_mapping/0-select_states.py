#!/usr/bin/python3
# Usage: ./0-select_states.py <mysql username> \
#                            <mysql password> \
#                            <database name>
import sys
import MySQLdb
'''
lists all states with a name starting
with N (upper N) from the database
hbtn_0e_0_usa
'''
if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost", port=3306, user=arg[1],
            passwd=arg[2], database=arg[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM `states` ORDER BY id ASC"
            )
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
