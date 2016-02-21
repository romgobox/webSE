#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_channels_type():
    channels_type_sql = '''
    SELECT 
        ct.id, 
        ct.type, 
        ct.short_type
    FROM
        channels_type ct
    '''
    cur, con = get_db()
    cur.execute(channels_type_sql)
    channels_types = cur.fetchall()
    channels_types_list = []
    for row in channels_types:
        channels_type = dict(row)
        channels_types_list.append(channels_type)
    return channels_types_list
    