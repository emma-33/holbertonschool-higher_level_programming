#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument"""

import sys
import MySQLdb


def main():
    """Main method to list all states where name matches the argument"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT id, name FROM `states`
                WHERE name LIKE BINARY '{}'
                ORDER BY id;""".format(sys.argv[4]))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
