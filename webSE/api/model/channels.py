#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_channels():
    channels_sql = '''
    SELECT
        ch.id, 
        ch.ch_desc, 
        ch.ch_ip, 
        ch.type_id, 
        ch.ch_port,
        ch.ch_settings,
        ch.is_active,
    FROM channels ch;
    '''
    cur, con = get_db()
    cur.execute(channels_sql)
    channels = cur.fetchall()
    channels_list = []
    for row in channels:
        channel = dict(row)
        channel['ch_settings'] = json.loads(channel['ch_settings'])
        channels_list.append(channel)
    return channels_list

def add_channel(data):
    channel_sql = u'''
    INSERT INTO channels 
    VALUES(
        Null, 
        '{ch_desc}', 
        '{ch_ip}',
        {type_id}, 
        {ch_port},  
        '{ch_settings}',
        {is_active}) 
    '''.format(
            ch_desc=data['ch_desc'], 
            ch_ip=data['ch_ip'], 
            type_id=data['type_id'],
            ch_port=data['ch_port'], 
            ch_settings=json.dumps(data['ch_settings']),
            is_active=data['is_active']) 

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(channel_sql)
        con.commit()
        data['id'] = cur.lastrowid
        response = data
        response['status'] = u'Добавлен новый канал опроса'
    except Exception, e:
        response['status'] = u'Канал опроса не добавлен. Причина: {e}'.format(e=e)
    return response

def update_channel(chID, data):
    channel_sql = u'''
    UPDATE channels
    SET 
        ch_desc='{ch_desc}', 
        ch_ip='{ch_ip}', 
        type_id={type_id},
        ch_port='{ch_port}', 
        ch_settings='{ch_settings}',
        is_active={is_active}
    WHERE id={id}
    '''.format(
            ch_desc=data['ch_desc'], 
            ch_ip=data['ch_ip'], 
            type_id=data['type_id'],
            ch_port=data['ch_port'], 
            ch_settings=json.dumps(data['ch_settings']),
            is_active=data['is_active'],
            id=chID)

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(channel_sql)
        con.commit()
        response['status'] = u'Сохранено'
    except Exception, e:
        response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
    return response

def del_channel(id):
    channel_sql = u'''
    DELETE FROM channels
    WHERE id={id}
    '''.format(id=id)
    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(channel_sql)
        con.commit()
        response['status'] = u'Удален канал опроса'
    except Exception, e:
        response['status'] = u'Канал опроса не удален. Причина: {e}'.format(e=e)
    return response