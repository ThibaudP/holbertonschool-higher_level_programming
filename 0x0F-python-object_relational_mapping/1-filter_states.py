#!/usr/bin/python3
"""1-filter_states"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
