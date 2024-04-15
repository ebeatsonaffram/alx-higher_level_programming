#!/usr/bin/python3
"""

A script that takes in argument and display all values in the states
table of hbtn_0e_0_usa and also safe from MySQL injections.

"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
