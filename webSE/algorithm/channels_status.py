#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from datetime import datetime
from webSE.api.model import get_db

'''
Статусы каналов:
    0 - Новый, 
'''
channel_status_dict = {
   -1: u'Новый',
    0: u'Параметры канала изменены',
    1: u'Соединение установлено',
    2: u'Идет опрос приборов учета',
    3: u'Опрос приборов учета завершен',
    4: u'Соединение не было установлено'
}

def insertChannelStatus(cur, con, channel_id, status_code, status_string=None):
    global channel_status_dict
    status_string = status_string or channel_status_dict[status_code]
    channel_status_sql = u'''
        INSERT INTO channels_status 
        VALUES(
            DEFAULT,
            {channel_id}, 
            '{status_datetime}',
            {status_code}, 
            '{status_string}')  
        '''.format(
                channel_id=channel_id, 
                status_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                status_code=status_code,
                status_string=status_string)
        
    cur.execute(channel_status_sql)
    con.commit()

def updateChannelStatus(cur, con, channel_id, status_code, status_string=None):
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
                status_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                status_code=status_code,
                status_string=status_string)
        
    cur.execute(channel_status_sql)
    con.commit()

