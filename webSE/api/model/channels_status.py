#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import datetime
from webSE.api.model import get_db


channel_status_dict = {
   -1: u'Новый',
    0: u'Параметры канала изменены',
    1: u'Соединение установлено',
    2: u'Идет опрос приборов учета',
    3: u'Опрос приборов учета завершен',
    4: u'Соединение не было установлено'
}

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
        channel_status['status_datetime'] = channel_status['status_datetime'].strftime('%d.%m.%y %H:%M:%S')
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


def insert_channel_status(channel_id, status_code, cur=None, con=None, status_string=None):
    global channel_status_dict
    status_string = status_string or channel_status_dict[status_code]
    channel_status_sql = u'''
        INSERT INTO channels_status 
        VALUES(
            Null, 
            {channel_id}, 
            '{status_datetime}',
            {status_code}, 
            '{status_string}')  
        '''.format(
                channel_id=channel_id, 
                status_datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                status_code=status_code,
                status_string=status_string)
        
    cur.execute(channel_status_sql)
    con.commit()

def update_channel_status(channel_id, status_code, cur=None, con=None, status_string=None):
    if not cur and not con:
        cur, con = get_db()
    global channel_status_dict
    status_string = status_string or channel_status_dict[status_code]
    channel_status_sql = u'''
        UPDATE channels_status 
        SET
            status_datetime='{status_datetime}',
            status_code={status_code}, 
            status_string='{status_string}' 
        WHERE channel_id={channel_id} 
        '''.format(
                channel_id=channel_id, 
                status_datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                status_code=status_code,
                status_string=status_string)
        
    cur.execute(channel_status_sql)
    con.commit()
    