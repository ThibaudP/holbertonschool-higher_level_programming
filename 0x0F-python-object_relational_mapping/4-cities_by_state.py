#!/usr/bin/python3
import MySQLdb
from sys import argv


def main(mysql_user, mysql_pwd, db_name):
    """main function"""
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_pwd, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states ON states.id = cities.state_id\
                    ORDER BY cities.id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        main(argv[1], argv[2], argv[3])
