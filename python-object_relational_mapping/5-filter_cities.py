#!/usr/bin/python3
"""Lists all cities by state from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


def main():
    """Main method to list all cities by state"""
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])

        cur = db.cursor()
        cur.execute("""SELECT cities.name
                    FROM `cities`
                    JOIN `states`
                    ON cities.state_id = states.id
                    WHERE states.name = '{}'
                    ORDER BY cities.id;""".format(sys.argv[4]))

        states = cur.fetchall()

        if states is not None:
            print(", ".join([state[0] for state in states]))

        cur.close()
        db.close()

    else:
        return


if __name__ == '__main__':
    main()
