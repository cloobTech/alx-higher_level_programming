#!/usr/bin/python3
""""  a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(
            host="localhost",
            port=3306, user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cur = conn.cursor()
    cur.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (sys.argv[4],)
    )
    query_rows = cur.fetchall()
    row = [query_rows[i][0] for i in range(len(query_rows))]
    row = ", ".join(row)
    print(row)
    cur.close()
    conn.close()
