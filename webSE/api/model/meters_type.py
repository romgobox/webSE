#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_meters_type():
    meters_type_sql = '''
    SELECT 
        mt.id, 
        mt.type, 
        mt.short_type,
        mt.protocol_id
    FROM
        meters_type mt
    '''
    cur, con = get_db()
    cur.execute(meters_type_sql)
    meters_types = cur.fetchall()
    meters_types_list = []
    for row in meters_types:
        meters_type = dict(row)
        meters_types_list.append(meters_type)
    return meters_types_list
    