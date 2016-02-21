#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_channels_status():
    channels_status_sql = '''
    SELECT 
        cs.id, 
        cs.channel_id, 
        cs.status_datetime, 
        cs.status_code, 
        cs.status_string
    FROM
        channels_status cs
    '''
    cur, con = get_db()
    cur.execute(channels_status_sql)
    channels_statuses = cur.fetchall()
    channels_statuses_list = []
    for row in channels_statuses:
        channel_status = dict(row)
        channels_statuses_list.append(channel_status)
    return channels_statuses_list

def get_channel_status(channel_id):
    channel_status_sql = '''
    SELECT 
        cs.id, 
        cs.channel_id, 
        cs.status_datetime, 
        cs.status_code, 
        cs.status_string
    FROM
        channels_status cs
    WHERE channel_id={channel_id}
    '''.format(channel_id=channel_id)

    cur, con = get_db()
    cur.execute(channel_status_sql)
    channel_status = dict(cur.fetchone())
    return channel_status
    