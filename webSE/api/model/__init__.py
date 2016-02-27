#! /usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import ConfigParser
import os

config_file = os.path.abspath(os.path.join(__file__ ,"../../..")) + '/config.ini'
parser = ConfigParser.SafeConfigParser()
parser.read(config_file)


def get_db():
    con = MySQLdb.connect(host=parser.get('DB', 'host'),
                            user=parser.get('DB', 'user'),
                            passwd=parser.get('DB', 'password'),
                            db=parser.get('DB', 'schema'),
                            cursorclass=MySQLdb.cursors.DictCursor)
    cur = con.cursor()

    con.set_character_set('utf8')
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    return cur, con
