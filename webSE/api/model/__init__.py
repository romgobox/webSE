#! /usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors


def get_db():
    con = MySQLdb.connect(host='localhost',
                            user='webse',
                            passwd='webse',
                            db='webamr',
                            cursorclass=MySQLdb.cursors.DictCursor)
    cur = con.cursor()

    con.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    return cur, con
