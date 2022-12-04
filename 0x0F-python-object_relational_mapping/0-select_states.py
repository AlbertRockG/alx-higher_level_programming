#!/usr/bin/python3


import MySQLdb
from sys import argv

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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cursor.fetchall()]
