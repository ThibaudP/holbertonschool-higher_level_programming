#!/usr/bin/python3
"""5-filter_cities"""
import MySQLdb
from sys import argv


def main(mysql_user, mysql_pwd, db_name, search):
    """main function"""
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_pwd, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT cities.name\
                    FROM cities\
                    INNER JOIN states ON states.id = cities.state_id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (search, ))

    rows = cursor.fetchall()
    list = []

    for row in rows:
        for col in row:
            list.append(col)

    print(", ".join(list))

    db.close()


if __name__ == "__main__":
    if len(argv) == 5:
        main(argv[1], argv[2], argv[3], argv[4])
