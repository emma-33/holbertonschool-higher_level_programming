#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


def main():
    """Main method to list all states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM `states` ORDER BY id;")

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
