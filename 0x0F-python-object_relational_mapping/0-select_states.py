#!/usr/bin/python3
""" Connecting to the hbtn_0e_0_usa database """
import MySQLdb
import sys


if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], 
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FR0M states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
