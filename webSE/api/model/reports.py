#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_protocols():
    protocols_sql = '''
    SELECT 
        pr.id, 
        pr.pr_name, 
        pr.pr_desc, 
        pr.pr_settings
    FROM
        protocols pr
    '''
    cur, con = get_db()
    cur.execute(protocols_sql)
    protocols = cur.fetchall()
    protocols_list = []
    for row in protocols:
        protocol = dict(row)
        protocol['pr_settings'] = json.loads(protocol['pr_settings'])
        protocols_list.append(protocol)
    return protocols_list
    