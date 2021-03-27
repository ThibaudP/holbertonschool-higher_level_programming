#!/usr/bin/python3
"""1-filter_states"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"

    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
